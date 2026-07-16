"""003 秒数转换。"""


def split_seconds(seconds):
    """把总秒数拆成小时、分钟和秒。"""
    hour = seconds // 3600
    remaining = seconds % 3600
    minute = remaining // 60
    second = remaining % 60
    return hour, minute, second


if __name__ == "__main__":
    print(split_seconds(3661))
