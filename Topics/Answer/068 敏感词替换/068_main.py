"""068 敏感词替换。"""

import re
from pathlib import Path


def replace_sensitive_words(input_path, output_path, words):
    """忽略大小写，把敏感词替换为等长星号。"""
    # re.escape() 防止敏感词中的特殊符号被当作正则语法。
    choices = "|".join(re.escape(word) for word in sorted(words, key=len, reverse=True))
    pattern = re.compile(choices, re.IGNORECASE)

    with open(input_path, "r", encoding="utf-8") as file:
        text = file.read()
    replaced, count = pattern.subn(lambda match: "*" * len(match.group()), text)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(replaced)
    return count


if __name__ == "__main__":
    folder = Path(__file__).parent
    count = replace_sensitive_words(folder / "sample.txt", folder / "cleaned.txt", ["bad"])
    print(f"共替换 {count} 次，请查看 cleaned.txt")
