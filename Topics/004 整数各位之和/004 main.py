n = -908
if n < 0:
	n = abs(n)
temp = n
sum = 0
count = 0
while (True):
	n //= 10
	if n == 0:
		break
	count += 1
for _ in range(count + 1):
	sum += temp % 10

	temp = temp // 10
print(sum)
