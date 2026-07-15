"""034 最长公共前缀。"""


def longest_common_prefix(words):
    """逐步缩短候选前缀，直到每个单词都以它开头。"""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))
