"""024 单词计数。"""


def count_words(text):
    """按任意连续空白分隔单词并返回数量。"""
    # split() 不传参数时，会自动忽略首尾和连续空白。
    words = text.split()
    return len(words)


if __name__ == "__main__":
    print(count_words("  one\ttwo\nthree  "))
