import math

a = float(input("请输入第一条边："))
b = float(input("请输入第二条边："))
c = float(input("请输入第三条边："))

# p = __________①__________
p = (a+b+c)/2
# s = __________②__________
s = math.sqrt(p*(p-a)*(p-b)*(p-c))

print("三角形面积为：{:.2f}".format(s))