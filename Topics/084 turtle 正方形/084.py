import turtle

side = int(input("请输入正方形边长："))

turtle.penup()
turtle.goto(0, 0)
turtle.setheading(0)
turtle.pendown()

turtle.pencolor("blue")
turtle.pensize(3)

for i in range(4):
    turtle.forward(side)
    turtle.left(90)

turtle.done()