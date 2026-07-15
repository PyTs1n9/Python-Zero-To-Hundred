"""009 出租车计费。"""

import math


def taxi_fare(distance):
    """根据行驶距离计算应付的整数金额。"""
    if distance <= 3:
        return 13
    # 超出部分不足 1 千米也按 1 千米计算。
    extra_kilometres = math.ceil(distance - 3)
    amount = 13 + extra_kilometres * 2.3
    # 金额非负，用 +0.5 后取整实现常见的四舍五入。
    return int(amount + 0.5)


if __name__ == "__main__":
    print(taxi_fare(4.2))
