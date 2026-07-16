"""076 数学函数报告。"""

import math


def math_report(n, k):
    """返回阶乘、最大公约数和组合数。"""
    combination = 0 if k > n else math.comb(n, k)
    return {
        "factorial": math.factorial(n),
        "gcd": math.gcd(n, k),
        "combination": combination,
    }


if __name__ == "__main__":
    print(math_report(5, 2))
