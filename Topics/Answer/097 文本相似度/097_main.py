"""097 文本相似度。需要先安装 jieba。"""

import jieba


def useful_word_set(text, stopwords):
    """返回过滤停用词、单字符词后的词语集合。"""
    return {
        word
        for word in jieba.lcut(text)
        if len(word.strip()) > 1
        and word not in stopwords
        and any(character.isalnum() for character in word)
    }


def jaccard_similarity(text1, text2, stopwords):
    """计算两段文本词语集合的杰卡德相似度。"""
    first = useful_word_set(text1, stopwords)
    second = useful_word_set(text2, stopwords)
    union = first | second
    if not union:
        return 1.0
    return round(len(first & second) / len(union), 4)


if __name__ == "__main__":
    first = "我喜欢学习Python编程"
    second = "他正在学习Python"
    print(jaccard_similarity(first, second, {"喜欢", "正在"}))
