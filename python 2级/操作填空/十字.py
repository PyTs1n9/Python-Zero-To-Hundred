# 使用 turtle 库的 turtle.fd() 函数和 turtle.seth() 函数绘制一个十字形，每个方向的长度为100像素。
import turtle
for i in range(4):
    turtle.fd(100)
    turtle.fd(-100)
    turtle.seth((i+1)*90)
turtle.done()