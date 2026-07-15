"""065 CSV 学生成绩。"""

import csv
from pathlib import Path


def student_averages(path):
    """读取三科成绩，返回按平均分和姓名排序的列表。"""
    result = []
    with open(path, "r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            scores = [int(row["chinese"]), int(row["math"]), int(row["english"])]
            average = round(sum(scores) / 3, 2)
            result.append((row["name"], average))
    return sorted(result, key=lambda item: (-item[1], item[0]))


if __name__ == "__main__":
    sample = Path(__file__).with_name("scores.csv")
    print(student_averages(sample))
