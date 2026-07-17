def gcd(a, b):
	a = abs(a)
	b = abs(b)
	while b:
		a, b = b, a % b
	return a

def lcm(a,b):
	if a==0 or b==0:
		return 0
	return abs(a//gcd(a,b)*b)

if __name__ == '__main__':
    print(lcm(-4,6))