"""021 字符串反转。"""


def reverse_string(text):
    """使用切片返回反转后的字符串。"""
    return text[::-1]


if __name__ == "__main__":
    print(reverse_string("Python"))
