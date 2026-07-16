"""063 筛选关键行。"""

from pathlib import Path


def filter_lines(input_path, output_path, keyword):
    """忽略大小写，把包含关键词的行写入新文件。"""
    count = 0
    lowered_keyword = keyword.casefold()
    with open(input_path, "r", encoding="utf-8") as source, open(
        output_path, "w", encoding="utf-8"
    ) as target:
        for line in source:
            if lowered_keyword in line.casefold():
                target.write(line)
                count += 1
    return count


if __name__ == "__main__":
    folder = Path(__file__).parent
    count = filter_lines(folder / "sample.txt", folder / "filtered.txt", "python")
    print(f"匹配到 {count} 行，请查看 filtered.txt")
