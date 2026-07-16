"""012 九九乘法表。"""


def multiplication_table():
    """返回九九乘法表，每个列表元素代表一行。"""
    lines = []
    for row in range(1, 10):
        expressions = []
        for column in range(1, row + 1):
            expressions.append(f"{column}×{row}={column * row}")
        lines.append(" ".join(expressions))
    return lines


if __name__ == "__main__":
    for line in multiplication_table():
        print(line)
