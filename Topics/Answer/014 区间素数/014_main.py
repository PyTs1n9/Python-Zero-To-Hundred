"""014 区间素数。"""

import math


def is_prime(n):
    """供主函数复用的素数判断函数。"""
    if n < 2:
        return False
    for divisor in range(2, math.isqrt(n) + 1):
        if n % divisor == 0:
            return False
    return True


def primes_in_range(left, right):
    """返回闭区间中的全部素数。"""
    return [number for number in range(left, right + 1) if is_prime(number)]


if __name__ == "__main__":
    print(primes_in_range(10, 20))
