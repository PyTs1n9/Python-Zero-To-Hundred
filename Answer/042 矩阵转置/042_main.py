"""042 矩阵转置。"""


def transpose(matrix):
    """把矩阵的行和列交换。"""
    row_count = len(matrix)
    column_count = len(matrix[0])
    result = []
    for column in range(column_count):
        new_row = []
        for row in range(row_count):
            new_row.append(matrix[row][column])
        result.append(new_row)
    return result


if __name__ == "__main__":
    print(transpose([[1, 2, 3], [4, 5, 6]]))
