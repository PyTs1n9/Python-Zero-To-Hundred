import random

code = ""

for i in range(4):
    # n = __________①__________
	n = random.randint(0,9)
	# code = __________②__________
	code = code + str(n)

print("验证码：", code)

user_code = input("请输入验证码：")

# if __________③__________:
if (user_code == code):
    print("验证码正确")
else:
    print("验证码错误")