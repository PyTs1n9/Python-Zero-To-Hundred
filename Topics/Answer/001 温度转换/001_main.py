"""001 温度转换。"""


def celsius_to_fahrenheit(celsius):
    """把摄氏温度转换为华氏温度，并返回两位小数字符串。"""
    fahrenheit = celsius * 1.8 + 32
    return f"{fahrenheit:.2f}"


if __name__ == "__main__":
    # 修改这里的数字，可以测试其他温度。
    print(celsius_to_fahrenheit(36.5))
