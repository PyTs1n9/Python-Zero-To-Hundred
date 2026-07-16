"""090 中文词频统计。需要先安装 jieba。"""

import jieba


def is_useful_word(word):
    """有效词长度大于 1，并且至少含一个字母或数字。"""
    return len(word.strip()) > 1 and any(character.isalnum() for character in word)


def chinese_word_frequency(text):
    """使用 jieba 分词并按次数降序、词语升序排列。"""
    counts = {}
    for word in jieba.lcut(text):
        if is_useful_word(word):
            counts[word] = counts.get(word, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))


if __name__ == "__main__":
    print(chinese_word_frequency("学习Python，快乐学习Python。"))
