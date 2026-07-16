"""087 turtle 彩色螺旋线。运行本文件会打开绘图窗口。"""

import turtle


def draw_spiral(steps, gap, colors):
    """绘制线段逐渐变长的方形螺旋线。"""
    pen = turtle.Turtle()
    pen.speed(0)
    for index in range(steps):
        pen.pencolor(colors[index % len(colors)])
        pen.forward((index + 1) * gap)
        pen.right(90)
    return pen


if __name__ == "__main__":
    draw_spiral(40, 5, ["red", "blue", "green", "orange"])
    turtle.done()
