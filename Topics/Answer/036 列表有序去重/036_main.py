"""036 列表有序去重。"""


def unique_in_order(items):
    """去除重复元素，同时保留第一次出现的顺序。"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    print(unique_in_order([3, 1, 3, 2, 1]))
