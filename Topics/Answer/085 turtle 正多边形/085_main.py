"""085 turtle 正多边形。运行本文件会打开绘图窗口。"""

import turtle


def draw_regular_polygon(n, side, color):
    """绘制并填充一个正 n 边形。"""
    pen = turtle.Turtle()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(n):
        pen.forward(side)
        pen.left(360 / n)
    pen.end_fill()
    return pen


if __name__ == "__main__":
    draw_regular_polygon(6, 60, "yellow")
    turtle.done()
