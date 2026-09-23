# 使用 turtle 库的 turtle.fd() 函数和 turtle.left() 函数绘制一个边长为200像素的正方形，
# 并在正方形的四个顶点处绘制一个紧挨正方形的圆形。

import turtle
turtle.pensize(2)
for i in range(4):
    turtle.fd(200)
    turtle.left(90)
turtle.left(-45)
turtle.circle(100*pow(2,0.5))
turtle.done()