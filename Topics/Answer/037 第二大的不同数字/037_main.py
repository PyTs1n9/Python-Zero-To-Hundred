"""037 第二大的不同数字。"""


def second_largest_distinct(nums):
    """返回第二大的不同数字，不存在时返回 None。"""
    distinct_numbers = sorted(set(nums), reverse=True)
    if len(distinct_numbers) < 2:
        return None
    return distinct_numbers[1]


if __name__ == "__main__":
    print(second_largest_distinct([2, 3, 1, 3]))
