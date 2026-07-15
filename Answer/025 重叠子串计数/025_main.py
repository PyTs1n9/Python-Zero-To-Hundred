"""025 重叠子串计数。"""


def count_overlapping(text, pattern):
    """统计 pattern 在 text 中出现的次数，包含重叠情况。"""
    count = 0
    start = 0
    while True:
        position = text.find(pattern, start)
        if position == -1:
            break
        count += 1
        # 只前进一位，因此不会漏掉重叠的匹配。
        start = position + 1
    return count


if __name__ == "__main__":
    print(count_overlapping("aaaa", "aa"))
