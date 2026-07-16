"""060 约瑟夫环。"""


def josephus_order(n, k):
    """模拟报数过程，返回所有人的退出顺序。"""
    people = list(range(1, n + 1))
    result = []
    index = 0
    while people:
        # 当前人从 1 开始报数，所以移动 k - 1 位。
        index = (index + k - 1) % len(people)
        result.append(people.pop(index))
    return result


if __name__ == "__main__":
    print(josephus_order(5, 2))
