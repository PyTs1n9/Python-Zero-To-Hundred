"""015 水仙花数。"""


def narcissistic_numbers(left, right):
    """返回区间内的所有三位水仙花数。"""
    answers = []
    for number in range(left, right + 1):
        hundreds = number // 100
        tens = number // 10 % 10
        ones = number % 10
        if hundreds ** 3 + tens ** 3 + ones ** 3 == number:
            answers.append(number)
    return answers


if __name__ == "__main__":
    print(narcissistic_numbers(100, 500))
