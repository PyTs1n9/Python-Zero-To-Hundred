"""089 jieba 三种分词模式。需要先安装 jieba。"""

import jieba


def three_cut_modes(text):
    """分别返回精确、全模式和搜索引擎模式的分词结果。"""
    precise = [word for word in jieba.lcut(text) if word.strip()]
    full = [word for word in jieba.lcut(text, cut_all=True) if word.strip()]
    search = [word for word in jieba.lcut_for_search(text) if word.strip()]
    return {"precise": precise, "full": full, "search": search}


if __name__ == "__main__":
    print(three_cut_modes("我来到北京清华大学"))
