"""082 日期间隔天数。"""

import time


def days_between(date1, date2):
    """计算两个 YYYY-MM-DD 日期相隔的完整天数。"""
    first = time.mktime(time.strptime(date1, "%Y-%m-%d"))
    second = time.mktime(time.strptime(date2, "%Y-%m-%d"))
    return int(abs(second - first) / 86400)


if __name__ == "__main__":
    print(days_between("2024-03-01", "2024-02-28"))
