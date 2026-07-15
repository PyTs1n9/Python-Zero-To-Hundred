"""017 最小公倍数。"""


def greatest_common_divisor(a, b):
    """使用辗转相除法计算最大公约数。"""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
    """计算两个整数的最小公倍数。"""
    if a == 0 or b == 0:
        return 0
    # 先除后乘，可以让中间结果更小。
    return abs(a // greatest_common_divisor(a, b) * b)


if __name__ == "__main__":
    print(least_common_multiple(-4, 6))
