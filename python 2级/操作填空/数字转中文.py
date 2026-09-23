# 输入示例：
# 9081726354
#
# 输出示例：
# 九〇八一七二六三五四
n = input()
s = "〇一二三四五六七八九"
for c in "0123456789":
     n = n.replace(c,s[int(c):int(c)+1])
print(n)