"""066 CSV 销售汇总。"""

import csv
from pathlib import Path


def sales_summary(path):
    """按商品累计销售额并排序。"""
    totals = {}
    with open(path, "r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            amount = int(row["quantity"]) * float(row["price"])
            product = row["product"]
            totals[product] = totals.get(product, 0) + amount

    result = [(product, round(amount, 2)) for product, amount in totals.items()]
    return sorted(result, key=lambda item: (-item[1], item[0]))


if __name__ == "__main__":
    sample = Path(__file__).with_name("sales.csv")
    print(sales_summary(sample))
