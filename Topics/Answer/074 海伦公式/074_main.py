"""074 海伦公式。"""

import math


def triangle_area(a, b, c):
    """能组成三角形时返回面积，否则返回 None。"""
    if min(a, b, c) <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return None
    half_perimeter = (a + b + c) / 2
    area = math.sqrt(
        half_perimeter
        * (half_perimeter - a)
        * (half_perimeter - b)
        * (half_perimeter - c)
    )
    return round(area, 2)


if __name__ == "__main__":
    print(triangle_area(3, 4, 5))
