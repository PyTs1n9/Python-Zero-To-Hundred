"""075 一元二次方程。"""

import math


def solve_equation(a, b, c):
    """求 ax²+bx+c=0 的实数解。"""
    if a == 0:
        if b == 0:
            return "ALL_REAL" if c == 0 else []
        return [round(-c / b, 6)]

    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return []
    root = math.sqrt(discriminant)
    answers = {round((-b - root) / (2 * a), 6), round((-b + root) / (2 * a), 6)}
    # 避免输出看起来奇怪的 -0.0。
    return sorted(0.0 if answer == 0 else answer for answer in answers)


if __name__ == "__main__":
    print(solve_equation(1, -3, 2))
