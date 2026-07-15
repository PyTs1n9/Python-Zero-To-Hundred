"""039 合并有序列表。"""


def merge_sorted(a, b):
    """使用双指针合并两个非递减列表。"""
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    # 至少有一个列表已经走完，把另一个列表的剩余部分补上。
    result.extend(a[i:])
    result.extend(b[j:])
    return result


if __name__ == "__main__":
    print(merge_sorted([1, 2, 4], [1, 3, 4]))
