def is_sxh(num):
	ge = num % 10
	shi = num % 100 // 10
	bai = num // 100
	if num == (ge ** 3 + shi ** 3 + bai ** 3):
		return True
	return None


def sxh_range(left, right):
	return [i for i in range(left,right+1) if is_sxh(i)]

if __name__ == '__main__':
	print(sxh_range(100,153))