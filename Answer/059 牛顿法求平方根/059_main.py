"""059 牛顿法求平方根。"""


def newton_square_root(x, epsilon):
    """使用牛顿迭代法求非负数的平方根。"""
    if x == 0:
        return 0.0

    current = x if x >= 1 else 1.0
    while True:
        next_value = (current + x / current) / 2
        if abs(next_value - current) < epsilon:
            return next_value
        current = next_value


if __name__ == "__main__":
    print(round(newton_square_root(2, 0.000001), 6))
