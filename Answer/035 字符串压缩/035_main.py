"""035 字符串压缩。"""


def compress_string(text):
    """把连续相同字符压缩为“字符+次数”。"""
    if not text:
        return ""

    parts = []
    current = text[0]
    count = 1
    for character in text[1:]:
        if character == current:
            count += 1
        else:
            parts.append(f"{current}{count}")
            current, count = character, 1
    parts.append(f"{current}{count}")
    return "".join(parts)


if __name__ == "__main__":
    print(compress_string("aaabbc"))
