"""006 闰年判断。"""


def is_leap_year(year):
    """闰年返回 True，否则返回 False。"""
    divisible_by_400 = year % 400 == 0
    divisible_by_4_not_100 = year % 4 == 0 and year % 100 != 0
    return divisible_by_400 or divisible_by_4_not_100


if __name__ == "__main__":
    print(is_leap_year(2000))
    print(is_leap_year(1900))
