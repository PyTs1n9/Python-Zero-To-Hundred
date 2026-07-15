"""007 成绩等级。"""


def grade_level(score):
    """把 0～100 的成绩转换为 A～E 等级。"""
    if score < 0 or score > 100:
        return "ERROR"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "E"


if __name__ == "__main__":
    print(grade_level(86))
