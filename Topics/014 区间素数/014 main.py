import math


def is_prime(n):
	"""供主函数复用的素数判断函数。"""
	if n < 2:
		return False
	for divisor in range(2, math.isqrt(n) + 1):
		if n % divisor == 0:
			return False
	return True


def primes_in_range(left, right):
	return [number for number in range(left, right + 1) if is_prime(number)]


if __name__ == '__main__':
	print(primes_in_range(1, 2))
