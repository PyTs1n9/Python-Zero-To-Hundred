# 使用 turtle 库绘制三个彩色的圆，圆的颜色按顺序从 color 列表中获取。
# 圆的圆心位于 (0,0) 坐标处，半径从里至外分别是10像素、30像素、60像素。

import turtle as t
color = ['red','green','blue']
rs = [10,30,60]

for i in range(len(rs)):
    t.penup()
    t.goto(0, -rs[i])
    t.pendown()
    t.pencolor(color[i])
    t.circle(rs[i])
t.done()
