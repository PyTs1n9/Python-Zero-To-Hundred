"""038 列表循环右移。"""


def rotate_right(nums, k):
    """返回循环右移 k 位后的新列表。"""
    if not nums:
        return []
    k %= len(nums)
    if k == 0:
        return nums[:]
    return nums[-k:] + nums[:-k]


if __name__ == "__main__":
    print(rotate_right([1, 2, 3, 4, 5], 2))
