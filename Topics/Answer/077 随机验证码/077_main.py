"""077 随机验证码。"""

import random
import string


def random_code(length):
    """生成至少包含一个字母和一个数字的验证码。"""
    if length < 2:
        return ""

    characters = [random.choice(string.ascii_uppercase), random.choice(string.digits)]
    all_characters = string.ascii_uppercase + string.digits
    for _ in range(length - 2):
        characters.append(random.choice(all_characters))
    # 打乱后，字母和数字不会总出现在固定位置。
    random.shuffle(characters)
    return "".join(characters)


if __name__ == "__main__":
    print(random_code(6))
