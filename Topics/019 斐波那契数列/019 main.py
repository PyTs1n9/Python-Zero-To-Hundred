def fb(n):
	pre, cur = 0, 1
	for _ in range(n):
		pre, cur = cur, pre + cur
	return pre

if __name__ == '__main__':
	print(fb(10))
