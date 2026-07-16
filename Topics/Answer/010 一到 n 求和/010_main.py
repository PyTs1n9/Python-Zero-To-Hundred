"""010 一到 n 求和。"""


def sum_to_n(n):
    """使用循环计算 1 到 n 的整数和。"""
    total = 0
    for number in range(1, n + 1):
        total += number
    return total


if __name__ == "__main__":
    print(sum_to_n(100))
