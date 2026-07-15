"""071 安全数字解析。"""


def parse_numbers(items):
    """把可转换项变成浮点数，并收集转换失败的原字符串。"""
    numbers = []
    failed = []
    for item in items:
        try:
            numbers.append(float(item))
        except ValueError:
            failed.append(item)
    return numbers, failed


if __name__ == "__main__":
    print(parse_numbers(["3.14", "abc", "2", ""]))
