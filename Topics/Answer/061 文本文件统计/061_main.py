"""061 文本文件统计。"""

from pathlib import Path


def text_file_stats(path):
    """统计 UTF-8 文本文件的行、单词和字符数量。"""
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    if text == "":
        line_count = 0
    else:
        line_count = text.count("\n")
        if not text.endswith("\n"):
            line_count += 1
    return {
        "lines": line_count,
        "words": len(text.split()),
        "characters": len(text),
    }


if __name__ == "__main__":
    sample = Path(__file__).with_name("sample.txt")
    print(text_file_stats(sample))
