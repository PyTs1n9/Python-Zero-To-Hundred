"""073 日期合法性检查。"""

import time


def weekday_or_invalid(date_text):
    """合法日期返回星期缩写，否则返回 INVALID。"""
    try:
        parsed = time.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        return "INVALID"
    # strptime 会接受部分不补零的输入，回写比较可保证格式严格一致。
    if time.strftime("%Y-%m-%d", parsed) != date_text:
        return "INVALID"
    return time.strftime("%a", parsed)


if __name__ == "__main__":
    print(weekday_or_invalid("2024-02-29"))
    print(weekday_or_invalid("2023-02-29"))
