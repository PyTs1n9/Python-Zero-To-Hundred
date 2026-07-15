"""092 中文文本分析报告。需要先安装 jieba。"""

import csv
from pathlib import Path

import jieba


def analyse_chinese_text(text_path, stopwords_path, output_path):
    """统计有效词，并把前 10 个高频词写入 CSV。"""
    with open(text_path, "r", encoding="utf-8") as file:
        text = file.read()
    with open(stopwords_path, "r", encoding="utf-8") as file:
        stopwords = {line.strip() for line in file if line.strip()}

    counts = {}
    for word in jieba.lcut(text):
        useful = (
            len(word.strip()) > 1
            and word not in stopwords
            and any(character.isalnum() for character in word)
        )
        if useful:
            counts[word] = counts.get(word, 0) + 1

    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    with open(output_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(ordered[:10])
    return {"total": sum(counts.values()), "unique": len(counts)}


if __name__ == "__main__":
    folder = Path(__file__).parent
    result = analyse_chinese_text(
        folder / "article.txt", folder / "stopwords.txt", folder / "result.csv"
    )
    print(result)
