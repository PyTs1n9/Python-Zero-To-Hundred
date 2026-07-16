"""057 递归二分查找。"""


def binary_search(nums, target):
    """返回目标值的下标，不存在时返回 -1。"""
    def search(left, right):
        if left > right:
            return -1
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if target < nums[middle]:
            return search(left, middle - 1)
        return search(middle + 1, right)

    return search(0, len(nums) - 1)


if __name__ == "__main__":
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))
