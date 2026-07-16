"""022 忽略符号的回文串。"""


def is_clean_palindrome(text):
    """忽略非字母数字字符和字母大小写后判断回文。"""
    cleaned_characters = []
    for character in text:
        if character.isalnum():
            cleaned_characters.append(character.lower())
    cleaned = "".join(cleaned_characters)
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_clean_palindrome("A man, a plan, a canal: Panama"))
