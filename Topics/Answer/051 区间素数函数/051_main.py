"""051 区间素数函数。"""

import math


def is_prime(n):
    """判断一个整数是否为素数。"""
    if n < 2:
        return False
    return all(n % divisor != 0 for divisor in range(2, math.isqrt(n) + 1))


def prime_summary(left, right):
    """汇总区间内的素数列表、数量与总和。"""
    primes = [number for number in range(left, right + 1) if is_prime(number)]
    return {"primes": primes, "count": len(primes), "sum": sum(primes)}


if __name__ == "__main__":
    print(prime_summary(2, 10))
