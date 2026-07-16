"""029 标题格式化。"""


def format_title(title):
    """让每个单词首字母大写，其余字母小写。"""
    formatted_words = []
    for word in title.split():
        formatted_words.append(word[0].upper() + word[1:].lower())
    return " ".join(formatted_words)


if __name__ == "__main__":
    print(format_title("python ZERO to WIN"))
