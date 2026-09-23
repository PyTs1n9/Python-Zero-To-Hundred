# 输入示例：
# 1.2,3.4,5.6,7.8,9.0
#
# 输出示例：
# 9.0
s = input("请输入一组数据: ")
ls = s.split(",")
lt = []
for i in ls:
    lt.append(eval(i))
print(max(lt))