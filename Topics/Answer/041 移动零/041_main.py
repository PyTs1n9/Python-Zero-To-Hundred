"""041 移动零。"""


def move_zeros(nums):
    """保持非零元素顺序，并把全部零放到末尾。"""
    non_zero = [number for number in nums if number != 0]
    zero_count = len(nums) - len(non_zero)
    return non_zero + [0] * zero_count


if __name__ == "__main__":
    print(move_zeros([0, 1, 0, 3, 12]))
