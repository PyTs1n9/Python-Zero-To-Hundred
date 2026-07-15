"""023 字符分类统计。"""


def classify_characters(text):
    """统计字母、数字、空白和其他字符的数量。"""
    result = {"letter": 0, "digit": 0, "space": 0, "other": 0}
    for character in text:
        if character.isalpha():
            result["letter"] += 1
        elif character.isdigit():
            result["digit"] += 1
        elif character.isspace():
            result["space"] += 1
        else:
            result["other"] += 1
    return result


if __name__ == "__main__":
    print(classify_characters("Py 3.10!"))
