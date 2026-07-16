"""079 随机抽样。"""

import random


def choose_winners(people, k, seed):
    """按随机种子抽取 k 个不重复的获奖者。"""
    if k < 0 or k > len(people):
        return []
    rng = random.Random(seed)
    return rng.sample(people, k)


if __name__ == "__main__":
    print(choose_winners(["A", "B", "C", "D"], 2, 1))
