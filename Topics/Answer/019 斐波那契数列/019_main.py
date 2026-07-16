"""019 斐波那契数列。"""


def fibonacci(n):
    """使用两个变量迭代计算第 n 个斐波那契数。"""
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


if __name__ == "__main__":
    print(fibonacci(10))
