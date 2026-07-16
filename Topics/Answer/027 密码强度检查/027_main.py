"""027 密码强度检查。"""


def check_password(password):
    """强密码返回“强”，否则返回缺失规则列表。"""
    missing = []
    if len(password) < 8:
        missing.append("长度")
    if not any(character.isupper() for character in password):
        missing.append("大写字母")
    if not any(character.islower() for character in password):
        missing.append("小写字母")
    if not any(character.isdigit() for character in password):
        missing.append("数字")
    if not any(not character.isalnum() for character in password):
        missing.append("特殊字符")
    return "强" if not missing else missing


if __name__ == "__main__":
    print(check_password("Py2026!x"))
    print(check_password("python"))
