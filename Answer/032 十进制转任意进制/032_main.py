"""032 十进制转任意进制。"""


def from_decimal(n, base):
    """使用除基取余法转换非负十进制整数。"""
    digits = "0123456789ABCDEF"
    if n == 0:
        return "0"

    result = []
    while n > 0:
        result.append(digits[n % base])
        n //= base
    # 余数是倒序产生的，因此最后需要反转。
    return "".join(reversed(result))


if __name__ == "__main__":
    print(from_decimal(255, 16))
