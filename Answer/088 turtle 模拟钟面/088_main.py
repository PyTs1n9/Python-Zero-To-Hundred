"""088 turtle 模拟钟面。运行本文件会打开绘图窗口。"""

import turtle


def draw_hand(pen, angle, length, color, width):
    """从圆心按钟表角度绘制一根指针。"""
    pen.penup()
    pen.goto(0, 0)
    # turtle 的 90 度朝上；减去角度即可实现顺时针旋转。
    pen.setheading(90 - angle)
    pen.pencolor(color)
    pen.pensize(width)
    pen.pendown()
    pen.forward(length)


def draw_clock(radius, hour, minute):
    """绘制外圆、12 个刻度、时针和分针。"""
    pen = turtle.Turtle()
    pen.speed(0)

    # circle() 会在海龟左侧画圆，所以从圆的最低点开始。
    pen.penup()
    pen.goto(0, -radius)
    pen.setheading(0)
    pen.pendown()
    pen.circle(radius)

    for index in range(12):
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(90 - index * 30)
        pen.forward(radius - 12)
        pen.pendown()
        pen.forward(12)

    minute_angle = minute * 6
    hour_angle = (hour % 12) * 30 + minute * 0.5
    draw_hand(pen, hour_angle, radius * 0.55, "black", 5)
    draw_hand(pen, minute_angle, radius * 0.8, "red", 3)
    pen.hideturtle()
    return pen


if __name__ == "__main__":
    draw_clock(150, 6, 30)
    turtle.done()
