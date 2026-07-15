"""091 停用词与高频词。需要先安装 jieba。"""

import jieba


def top_words(text, stopwords, k):
    """过滤停用词、单字符词和标点后返回前 k 个高频词。"""
    counts = {}
    for word in jieba.lcut(text):
        useful = (
            len(word.strip()) > 1
            and word not in stopwords
            and any(character.isalnum() for character in word)
        )
        if useful:
            counts[word] = counts.get(word, 0) + 1
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ordered[:k]


if __name__ == "__main__":
    text = "数据 数据 数据，分析需要清洗"
    print(top_words(text, {"需要"}, 2))
