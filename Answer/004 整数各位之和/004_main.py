"""004 整数各位之和。"""


def digit_sum(number):
    """忽略负号，计算整数各位数字之和。"""
    total = 0
    # abs() 去掉负号，str() 让我们可以逐个访问数字。
    for digit in str(abs(number)):
        total += int(digit)
    return total


if __name__ == "__main__":
    print(digit_sum(-908))
