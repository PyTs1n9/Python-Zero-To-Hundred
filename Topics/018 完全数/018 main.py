import math

def is_perfect_number(n):

    if n <= 1:
        return False

    sum_num = 1
    for divisor in range(2, math.isqrt(n) + 1):
        if n % divisor == 0:
            sum_num += divisor
            paired_divisor = n // divisor
            if paired_divisor != divisor:
                sum_num += paired_divisor
    return sum_num == n

if __name__ == "__main__":
    print(is_perfect_number(28))