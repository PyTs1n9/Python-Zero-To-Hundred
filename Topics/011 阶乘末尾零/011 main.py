n = 0
num = 1
for _ in range(2, n + 1):
	num *= _
count = 0

for _ in range(len(str(num)) + 1):
	if num % 10 == 0:
		num /= 10
		count += 1
	elif num % 10 != 0:
		break

