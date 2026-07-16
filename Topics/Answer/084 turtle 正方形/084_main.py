"""084 turtle 正方形。运行本文件会打开绘图窗口。"""

import turtle


def draw_square(side):
    """从画布中心开始绘制蓝色正方形。"""
    pen = turtle.Turtle()
    pen.pencolor("blue")
    pen.pensize(3)
    for _ in range(4):
        pen.forward(side)
        pen.left(90)
    return pen


if __name__ == "__main__":
    draw_square(100)
    turtle.done()
