"""064 合并并去重文件。"""

from pathlib import Path


def merge_unique_files(paths, output_path):
    """合并多份文本，忽略空行并按首次出现顺序去重。"""
    seen = set()
    unique_lines = []
    for path in paths:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                content = line.strip()
                if content and content not in seen:
                    seen.add(content)
                    unique_lines.append(content)

    with open(output_path, "w", encoding="utf-8") as file:
        if unique_lines:
            file.write("\n".join(unique_lines) + "\n")
    return unique_lines


if __name__ == "__main__":
    folder = Path(__file__).parent
    paths = [folder / "sample_a.txt", folder / "sample_b.txt"]
    print(merge_unique_files(paths, folder / "merged.txt"))
