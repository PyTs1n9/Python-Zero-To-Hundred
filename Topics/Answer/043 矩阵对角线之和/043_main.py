"""043 矩阵对角线之和。"""


def diagonal_sum(matrix):
    """计算主、副对角线之和，中心元素只算一次。"""
    size = len(matrix)
    total = 0
    for index in range(size):
        total += matrix[index][index]
        other_column = size - 1 - index
        if other_column != index:
            total += matrix[index][other_column]
    return total


if __name__ == "__main__":
    print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
