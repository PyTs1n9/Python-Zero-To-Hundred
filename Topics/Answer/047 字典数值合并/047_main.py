"""047 字典数值合并。"""


def merge_number_dicts(a, b):
    """合并字典，相同键的值相加，并按键升序插入。"""
    merged = {}
    for key in sorted(set(a) | set(b)):
        merged[key] = a.get(key, 0) + b.get(key, 0)
    return merged


if __name__ == "__main__":
    first = {"apple": 2, "banana": 3}
    second = {"banana": 4, "pear": 1}
    print(merge_number_dicts(first, second))
