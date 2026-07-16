"""013 素数判断。"""

import math


def is_prime(n):
    """判断 n 是否为素数。"""
    if n < 2:
        return False
    # 如果 n 有因子，至少有一个因子不会大于平方根。
    for divisor in range(2, math.isqrt(n) + 1):
        if n % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    print(is_prime(17))
