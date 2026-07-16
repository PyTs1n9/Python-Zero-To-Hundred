"""055 递归数字之和。"""


def recursive_digit_sum(n):
    """使用递归计算整数各位数字之和。"""
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + recursive_digit_sum(n // 10)


if __name__ == "__main__":
    print(recursive_digit_sum(-9008))
