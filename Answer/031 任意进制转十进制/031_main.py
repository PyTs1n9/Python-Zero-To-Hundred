"""031 任意进制转十进制。"""


def to_decimal(num, base):
    """用逐位累积法把 2～16 进制字符串转为十进制。"""
    digits = "0123456789ABCDEF"
    result = 0
    for character in num.upper():
        value = digits.index(character)
        result = result * base + value
    return result


if __name__ == "__main__":
    print(to_decimal("FF", 16))
