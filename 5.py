from functools import reduce


def lcm(n1, n2):
	return (n1 * n2) / (gcd(n1, n2) if n1 > n2 else gcd(n2, n1))


def gcd(n1, n2):
	if n1 % n2:
		return gcd(n2, n1 % n2)
	return n2


a = []
for i in range(20):
	a.append(i + 1)
print(reduce(lcm, a))
