weight = 90
height = 1.70
BMI = weight / height ** 2

if BMI < 18.5:
	print("偏瘦")
elif BMI < 24:
	print("正常")
elif BMI < 28:
	print("偏胖")
else:
	print("肥胖")
