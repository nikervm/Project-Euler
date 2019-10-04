def kolatz(n):
	if n % 2 == 0:
		return n / 2
	return 3 * n + 1


def count_elems(number, b):
	counter = 1
	number = int(kolatz(number))
	while number > len(b):
		counter += 1
		number = int(kolatz(number))
	counter += b[number - 1]
	return counter


i = 2
b = [1]
while i < 1000000:
	b.append(count_elems(i, b))
	i += 1
print(b.index(max(b)) + 1)
