"""099 多文件中文词频。需要先安装 jieba。"""

import csv
from pathlib import Path

import jieba


def analyse_text_directory(directory, stopwords_path, output_csv):
    """统计目录中全部 TXT 文件的中文词频。"""
    with open(stopwords_path, "r", encoding="utf-8") as file:
        stopwords = {line.strip() for line in file if line.strip()}

    text_files = sorted(
        (
            path
            for path in Path(directory).iterdir()
            if path.is_file() and path.suffix.lower() == ".txt"
        ),
        key=lambda path: path.name,
    )
    global_counts = {}
    per_file = {}
    total_words = 0

    for path in text_files:
        text = path.read_text(encoding="utf-8")
        current_count = 0
        for word in jieba.lcut(text):
            useful = (
                len(word.strip()) > 1
                and word not in stopwords
                and any(character.isalnum() for character in word)
            )
            if useful:
                global_counts[word] = global_counts.get(word, 0) + 1
                current_count += 1
        per_file[path.name] = current_count
        total_words += current_count

    top_words = sorted(global_counts.items(), key=lambda item: (-item[1], item[0]))[:20]
    with open(output_csv, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["word", "count"])
        writer.writerows(top_words)
    return {
        "files": len(text_files),
        "total_words": total_words,
        "per_file": per_file,
        "top_words": top_words,
    }


if __name__ == "__main__":
    folder = Path(__file__).parent
    result = analyse_text_directory(
        folder / "texts", folder / "stopwords.txt", folder / "word_count.csv"
    )
    print(result)
