"""081 UTC 时间格式化。"""

import time


def format_utc(timestamp):
    """把 Unix 时间戳转换为固定格式的 UTC 时间。"""
    utc_time = time.gmtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S UTC", utc_time)


if __name__ == "__main__":
    print(format_utc(0))
