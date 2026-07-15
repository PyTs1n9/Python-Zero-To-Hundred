"""048 集合关系报告。"""


def set_report(a, b):
    """返回两个列表对应集合的四种关系。"""
    set_a, set_b = set(a), set(b)
    return {
        "intersection": sorted(set_a & set_b),
        "union": sorted(set_a | set_b),
        "difference": sorted(set_a - set_b),
        "symmetric_difference": sorted(set_a ^ set_b),
    }


if __name__ == "__main__":
    print(set_report([1, 2, 2, 3], [2, 3, 4]))
