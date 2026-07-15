"""016 最大公约数。"""


def greatest_common_divisor(a, b):
    """使用辗转相除法计算最大公约数。"""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    print(greatest_common_divisor(48, 18))
