"""056 递归列表展平。"""


def flatten(items):
    """递归取出嵌套列表中的全部整数。"""
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    print(flatten([1, [2, [3, 4]], 5]))
