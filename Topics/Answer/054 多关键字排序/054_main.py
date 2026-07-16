"""054 多关键字排序。"""


def sort_students(students):
    """按成绩降序、年龄升序、姓名升序排列。"""
    # 成绩前加负号，就能在整体升序时实现成绩降序。
    return sorted(
        students,
        key=lambda student: (-student["score"], student["age"], student["name"]),
    )


if __name__ == "__main__":
    data = [
        {"name": "Li", "score": 90, "age": 20},
        {"name": "Wang", "score": 90, "age": 19},
        {"name": "An", "score": 85, "age": 19},
    ]
    print(sort_students(data))
