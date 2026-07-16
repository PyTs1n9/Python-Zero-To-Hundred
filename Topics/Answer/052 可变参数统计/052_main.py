"""052 可变参数统计。"""


def number_stats(*numbers):
    """统计任意数量数字的个数、总和和平均值。"""
    count = len(numbers)
    total = sum(numbers)
    average = None if count == 0 else round(total / count, 2)
    return {"count": count, "sum": total, "average": average}


if __name__ == "__main__":
    print(number_stats(1, 2, 3, 4))
    print(number_stats())
