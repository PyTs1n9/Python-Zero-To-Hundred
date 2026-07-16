"""018 完全数。"""

import math


def is_perfect_number(n):
    """判断正整数是否等于所有真因子之和。"""
    if n <= 1:
        return False

    divisor_sum = 1
    for divisor in range(2, math.isqrt(n) + 1):
        if n % divisor == 0:
            divisor_sum += divisor
            paired_divisor = n // divisor
            # 平方数的两个因子相同，只能加一次。
            if paired_divisor != divisor:
                divisor_sum += paired_divisor
    return divisor_sum == n


if __name__ == "__main__":
    print(is_perfect_number(28))
