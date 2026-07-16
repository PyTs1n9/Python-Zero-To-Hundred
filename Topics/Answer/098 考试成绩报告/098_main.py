"""098 考试成绩报告。"""

import csv
from pathlib import Path


def grade_level(score):
    """把成绩转换为 A、B、C、D、E。"""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "E"


def create_score_report(csv_path, report_path):
    """清洗成绩、计算统计值，并写出文本报告。"""
    students = []
    with open(csv_path, "r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            try:
                student_id = row["id"].strip()
                name = row["name"].strip()
                score = float(row["score"])
            except (KeyError, AttributeError, TypeError, ValueError):
                continue
            if not student_id or not name or not 0 <= score <= 100:
                continue
            students.append({"id": student_id, "name": name, "score": score})

    students.sort(key=lambda item: (-item["score"], item["id"]))
    grade_counts = {grade: 0 for grade in "ABCDE"}
    for index, student in enumerate(students):
        if index == 0 or student["score"] != students[index - 1]["score"]:
            rank = index + 1
        student["rank"] = rank
        student["grade"] = grade_level(student["score"])
        grade_counts[student["grade"]] += 1

    count = len(students)
    scores = [student["score"] for student in students]
    summary = {
        "count": count,
        "average": round(sum(scores) / count, 2) if count else 0,
        "max": max(scores) if count else 0,
        "min": min(scores) if count else 0,
        "pass_rate": round(sum(score >= 60 for score in scores) / count * 100, 2) if count else 0,
        "grades": grade_counts,
    }

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(f"有效人数:{summary['count']}\n")
        file.write(f"平均分:{summary['average']:.2f}\n")
        file.write(f"最高分:{summary['max']:g}\n")
        file.write(f"最低分:{summary['min']:g}\n")
        file.write(f"及格率:{summary['pass_rate']:.2f}%\n")
        file.write("等级人数:" + ",".join(f"{g}={grade_counts[g]}" for g in "ABCDE") + "\n")
        file.write("名次,学号,姓名,成绩,等级\n")
        for student in students:
            file.write(
                f"{student['rank']},{student['id']},{student['name']},"
                f"{student['score']:g},{student['grade']}\n"
            )
    return summary


if __name__ == "__main__":
    folder = Path(__file__).parent
    result = create_score_report(folder / "scores.csv", folder / "report.txt")
    print(result)
