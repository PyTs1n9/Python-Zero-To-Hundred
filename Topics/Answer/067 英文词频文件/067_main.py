"""067 英文词频文件。"""

import re
from pathlib import Path


def english_word_frequency(path):
    """统计只由英文字母组成的单词，忽略大小写。"""
    with open(path, "r", encoding="utf-8") as file:
        text = file.read().lower()

    counts = {}
    for word in re.findall(r"[a-z]+", text):
        counts[word] = counts.get(word, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))


if __name__ == "__main__":
    sample = Path(__file__).with_name("article.txt")
    print(english_word_frequency(sample))
