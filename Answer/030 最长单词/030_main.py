"""030 最长单词。"""


def longest_word(text):
    """返回最长单词；并列时保留最先出现的单词。"""
    answer = ""
    for word in text.split():
        # 只在严格更长时更新，所以并列时不会覆盖旧答案。
        if len(word) > len(answer):
            answer = word
    return answer


if __name__ == "__main__":
    print(longest_word("Python makes programming enjoyable"))
