"""002 圆的面积和周长。"""

import math


def circle_info(radius):
    """返回圆的面积和周长。"""
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    # round(数字, 2) 表示保留两位小数。
    return round(area, 2), round(perimeter, 2)


if __name__ == "__main__":
    print(circle_info(2.5))
