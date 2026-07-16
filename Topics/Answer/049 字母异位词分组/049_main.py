"""049 字母异位词分组。"""


def group_anagrams(words):
    """使用排序后的字母串作为分组键。"""
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    # 字典会保持键首次插入的顺序。
    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
