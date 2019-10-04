def prime(n):
	if not n % 2:
		return False
	if not n % 3:
		return False
	if not n % 5:
		return False
	if not n % 7:
		return False
	i = 7
	while i * i <= n:
		if not (n % i):
			return False
		i += 2
	return True


n, i, j = 10001, 4, 7
while i != n:
	j += 1
	if prime(j):
		i += 1
print(prime(j))
print(j)
