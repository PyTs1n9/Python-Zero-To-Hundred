"""086 turtle 五角星。运行本文件会打开绘图窗口。"""

import turtle


def draw_star(side, colors):
    """绘制彩色边线、金色填充的五角星。"""
    pen = turtle.Turtle()
    pen.fillcolor("gold")
    pen.begin_fill()
    for index in range(5):
        pen.pencolor(colors[index % len(colors)])
        pen.forward(side)
        pen.right(144)
    pen.end_fill()
    pen.hideturtle()
    return pen


if __name__ == "__main__":
    draw_star(150, ["red", "green", "blue"])
    turtle.done()
