"""062 添加行号。"""

from pathlib import Path


def add_line_numbers(input_path, output_path):
    """为输入文件的每一行添加四位行号。"""
    count = 0
    with open(input_path, "r", encoding="utf-8") as source, open(
        output_path, "w", encoding="utf-8"
    ) as target:
        for count, line in enumerate(source, start=1):
            # 去掉原行尾，再统一写入一个换行符。
            content = line.rstrip("\r\n")
            target.write(f"{count:04d}: {content}\n")
    return count


if __name__ == "__main__":
    folder = Path(__file__).parent
    total = add_line_numbers(folder / "sample.txt", folder / "numbered.txt")
    print(f"已写入 {total} 行，请查看 numbered.txt")
