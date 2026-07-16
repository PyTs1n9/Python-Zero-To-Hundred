"""026 合法标识符。"""

import keyword


def is_valid_variable_name(name):
    """判断字符串是否可以作为普通 Python 变量名。"""
    return name.isidentifier() and not keyword.iskeyword(name)


if __name__ == "__main__":
    print(is_valid_variable_name("student_2"))
    print(is_valid_variable_name("for"))
