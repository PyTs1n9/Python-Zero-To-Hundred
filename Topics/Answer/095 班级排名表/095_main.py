"""095 班级排名表。"""

import csv
from pathlib import Path


def class_ranking(path):
    """清洗成绩记录，并按总分生成竞赛排名。"""
    students = []
    with open(path, "r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            try:
                student_id = row["id"].strip()
                name = row["name"].strip()
                scores = [int(row[subject]) for subject in ("chinese", "math", "english")]
            except (KeyError, TypeError, ValueError):
                continue
            if not student_id or not name or any(score < 0 or score > 100 for score in scores):
                continue
            total = sum(scores)
            students.append(
                {"id": student_id, "name": name, "total": total, "average": round(total / 3, 2)}
            )

    students.sort(key=lambda item: (-item["total"], item["id"]))
    previous_total = None
    current_rank = 0
    for index, student in enumerate(students):
        if student["total"] != previous_total:
            current_rank = index + 1
            previous_total = student["total"]
        student["rank"] = current_rank
        # 重建字典，让返回字段采用题目给出的顺序。
        ordered = {
            "rank": student.pop("rank"),
            "id": student.pop("id"),
            "name": student.pop("name"),
            "total": student.pop("total"),
            "average": student.pop("average"),
        }
        student.update(ordered)
    return students


if __name__ == "__main__":
    sample = Path(__file__).with_name("scores.csv")
    print(class_ranking(sample))
