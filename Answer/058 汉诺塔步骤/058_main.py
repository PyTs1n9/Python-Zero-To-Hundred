"""058 汉诺塔步骤。"""


def hanoi_moves(n, source="A", helper="B", target="C"):
    """返回将 n 个圆盘从 source 移到 target 的全部步骤。"""
    if n == 1:
        return [f"{source}->{target}"]

    moves = hanoi_moves(n - 1, source, target, helper)
    moves.append(f"{source}->{target}")
    moves.extend(hanoi_moves(n - 1, helper, source, target))
    return moves


if __name__ == "__main__":
    print(hanoi_moves(2))
