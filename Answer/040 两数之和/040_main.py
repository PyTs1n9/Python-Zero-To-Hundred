"""040 两数之和。"""


def two_sum(nums, target):
    """用字典在一次遍历中找出答案下标。"""
    seen = {}
    for index, number in enumerate(nums):
        needed = target - number
        if needed in seen:
            return [seen[needed], index]
        seen[number] = index
    # 题目保证有答案，这一行只用于增强函数的完整性。
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
