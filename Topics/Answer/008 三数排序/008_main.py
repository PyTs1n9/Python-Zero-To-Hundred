"""008 三数排序。"""


def sort_three(a, b, c):
    """返回三个数字从小到大排列的新列表。"""
    numbers = [a, b, c]
    numbers.sort()
    return numbers


if __name__ == "__main__":
    print(sort_three(3, 1, 2))
