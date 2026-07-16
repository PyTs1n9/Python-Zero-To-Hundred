"""028 凯撒密码。"""


def shift_letter(character, shift, first_letter):
    """在同一大小写字母表内循环移动一个字母。"""
    offset = ord(character) - ord(first_letter)
    new_offset = (offset + shift) % 26
    return chr(ord(first_letter) + new_offset)


def caesar_encrypt(text, shift):
    """加密英文字母，其他字符保持不变。"""
    encrypted = []
    shift %= 26
    for character in text:
        if "A" <= character <= "Z":
            encrypted.append(shift_letter(character, shift, "A"))
        elif "a" <= character <= "z":
            encrypted.append(shift_letter(character, shift, "a"))
        else:
            encrypted.append(character)
    return "".join(encrypted)


if __name__ == "__main__":
    print(caesar_encrypt("Abc-Z", 2))
