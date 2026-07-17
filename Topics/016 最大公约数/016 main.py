def gcd(a, b):
	a, b = abs(a), abs(b)
	while b != 0:
		a, b = b, a % b
	return a

if __name__ == '__main__':
    print(gcd(48,18))
