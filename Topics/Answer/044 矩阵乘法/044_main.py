"""044 矩阵乘法。"""


def matrix_multiply(a, b):
    """按“左矩阵的行乘右矩阵的列”计算乘积。"""
    rows = len(a)
    shared_size = len(b)
    columns = len(b[0])
    result = [[0] * columns for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            for index in range(shared_size):
                result[row][column] += a[row][index] * b[index][column]
    return result


if __name__ == "__main__":
    print(matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
