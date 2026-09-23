# 使用 turtle 库的 turtle.fd() 函数和 turtle.seth() 函数绘制一个边长为40像素的正12边形。
import turtle
turtle.pensize(2)
d=0
for i in range(1, 13):
    turtle.fd(40)
    d += 30
    turtle.seth(d)
turtle.done()