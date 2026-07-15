"""072 安全四则运算。"""


def calculate(a, operator, b):
    """完成四则运算，并把常见错误转换为指定字符串。"""
    valid_number = (int, float)
    if (
        not isinstance(a, valid_number)
        or isinstance(a, bool)
        or not isinstance(b, valid_number)
        or isinstance(b, bool)
    ):
        return "INVALID_NUMBER"

    if operator not in {"+", "-", "*", "/"}:
        return "INVALID_OPERATOR"
    try:
        if operator == "+":
            return a + b
        if operator == "-":
            return a - b
        if operator == "*":
            return a * b
        return a / b
    except ZeroDivisionError:
        return "DIVISION_BY_ZERO"


if __name__ == "__main__":
    print(calculate(10, "/", 4))
    print(calculate(5, "/", 0))
