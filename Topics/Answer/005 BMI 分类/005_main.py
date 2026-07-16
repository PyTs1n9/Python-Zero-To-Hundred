"""005 BMI 分类。"""


def bmi_category(weight, height):
    """根据体重（千克）和身高（米）返回 BMI 分类。"""
    bmi = weight / height ** 2
    # 从小到大判断，每个区间只会进入一次。
    if bmi < 18.5:
        return "偏瘦"
    if bmi < 24:
        return "正常"
    if bmi < 28:
        return "偏胖"
    return "肥胖"


if __name__ == "__main__":
    print(bmi_category(60, 1.75))
