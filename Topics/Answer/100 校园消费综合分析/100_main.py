"""100 校园消费综合分析。"""

import csv
import json
import time
from pathlib import Path


def parse_time(time_text):
    """严格解析 YYYY-MM-DD HH:MM:SS，失败时抛出 ValueError。"""
    parsed = time.strptime(time_text, "%Y-%m-%d %H:%M:%S")
    if time.strftime("%Y-%m-%d %H:%M:%S", parsed) != time_text:
        raise ValueError("时间格式不完整")
    return parsed


def rounded_amount_dict(amounts):
    """按金额降序、名称升序排列，并统一保留两位小数。"""
    ordered = sorted(amounts.items(), key=lambda item: (-item[1], item[0]))
    return {name: round(amount, 2) for name, amount in ordered}


def analyse_consumption(csv_path, target_date, output_json):
    """清洗指定日期的消费数据，生成并写出综合报告。"""
    category_totals = {}
    student_totals = {}
    hourly_count = {f"{hour:02d}": 0 for hour in range(24)}
    valid_records = 0
    invalid_records = 0
    total_amount = 0.0

    with open(csv_path, "r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            try:
                time_text = row["time"].strip()
                student_id = row["student_id"].strip()
                category = row["category"].strip()
                amount = float(row["amount"])
                parsed_time = parse_time(time_text)
                if not student_id or not category or amount < 0:
                    raise ValueError("字段不合法")
            except (KeyError, AttributeError, TypeError, ValueError):
                invalid_records += 1
                continue

            record_date = time.strftime("%Y-%m-%d", parsed_time)
            if record_date != target_date:
                # 其他日期的合法记录既不参与统计，也不算非法记录。
                continue

            valid_records += 1
            total_amount += amount
            category_totals[category] = category_totals.get(category, 0) + amount
            student_totals[student_id] = student_totals.get(student_id, 0) + amount
            hour = time.strftime("%H", parsed_time)
            hourly_count[hour] += 1

    ordered_students = sorted(student_totals.items(), key=lambda item: (-item[1], item[0]))
    top3_students = [
        {"student_id": student_id, "amount": round(amount, 2)}
        for student_id, amount in ordered_students[:3]
    ]
    report = {
        "date": target_date,
        "valid_records": valid_records,
        "invalid_records": invalid_records,
        "total_amount": round(total_amount, 2),
        "average_amount": round(total_amount / valid_records, 2) if valid_records else 0.0,
        "category_amount": rounded_amount_dict(category_totals),
        "student_amount": rounded_amount_dict(student_totals),
        "top3_students": top3_students,
        "hourly_count": hourly_count,
    }

    with open(output_json, "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=2)
    return report


if __name__ == "__main__":
    folder = Path(__file__).parent
    result = analyse_consumption(
        folder / "consumption.csv", "2026-07-15", folder / "report.json"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
