"""078 骰子模拟。"""

import random


def simulate_dice(n, seed):
    """模拟掷两个骰子，并统计点数和 2～12 的次数。"""
    rng = random.Random(seed)
    counts = {total: 0 for total in range(2, 13)}
    for _ in range(n):
        total = rng.randint(1, 6) + rng.randint(1, 6)
        counts[total] += 1
    return counts


if __name__ == "__main__":
    print(simulate_dice(3, 0))
