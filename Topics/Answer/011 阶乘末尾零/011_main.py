"""011 阶乘末尾零。"""


def trailing_zeros_of_factorial(n):
    """先计算 n!，再统计末尾连续零的数量。"""
    factorial = 1
    for number in range(2, n + 1):
        factorial *= number

    zero_count = 0
    while factorial % 10 == 0:
        zero_count += 1
        factorial //= 10
    return zero_count


if __name__ == "__main__":
    print(trailing_zeros_of_factorial(10))
