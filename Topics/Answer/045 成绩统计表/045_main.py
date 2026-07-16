"""045 成绩统计表。"""


def score_summary(scores):
    """返回平均分、最高分、最低分和及格人数。"""
    average = round(sum(scores) / len(scores), 2)
    pass_count = sum(1 for score in scores if score >= 60)
    return {
        "average": average,
        "max": max(scores),
        "min": min(scores),
        "pass_count": pass_count,
    }


if __name__ == "__main__":
    print(score_summary([80, 95, 58, 67]))
