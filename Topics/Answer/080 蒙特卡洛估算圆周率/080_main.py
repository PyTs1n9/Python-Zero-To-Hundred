"""080 蒙特卡洛估算圆周率。"""

import random


def estimate_pi(n, seed):
    """用落入四分之一圆的随机点比例估算圆周率。"""
    if n == 0:
        return 0.0
    rng = random.Random(seed)
    inside = 0
    for _ in range(n):
        x, y = rng.random(), rng.random()
        if x ** 2 + y ** 2 <= 1:
            inside += 1
    return round(4 * inside / n, 6)


if __name__ == "__main__":
    print(estimate_pi(10000, 0))
