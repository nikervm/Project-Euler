import math
from collections import Counter


def isPrime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True


def get_next_prime(prime):
	prime += 1
	while not isPrime(prime):
		prime += 1
	return prime


def count_div(n):
	a = []
	while n != 1:
		i = 2
		if n % i == 0:
			a.append(i)
			n = n / i
		else:
			while n % i:
				i = get_next_prime(i)
			a.append(i)
			n = n / i
	b = [0]
	a = Counter(a)
	list_keys = list(a.keys())
	j = 2
	count = 0
	for i in list_keys:
		while j != i:
			j = get_next_prime(j)
			b.append(0)
			count += 1
		b[count] = a[i]
	amount = 1
	for i in range(len(b)):
		amount *= b[i] + 1
	return amount


i, number = 1, 1
while count_div(number) < 500:
	i += 1
	number += i
print(number)
