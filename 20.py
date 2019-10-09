def ten(a, pos):
	if pos == len(a) - 1:
		a.append(a[pos] // 10)
		a[pos] %= 10
		return
	a[pos + 1] += a[pos] // 10
	a[pos] %= 10


def hundred(a, pos):
	if pos == len(a) - 1:
		a.append(a[pos] // 10)
		a[pos] %= 10
		ten(a, pos + 1)
		return
	a[pos + 1] += a[pos] // 10
	a[pos] %= 10
	if 100 <= a[pos + 1] < 1000:
		hundred(a, pos + 1)
	if 10 <= a[pos + 1] < 100:
		ten(a, pos + 1)


n, a = 100, [1]
for i in range(1, n + 1):
	num = i
	for j in range(len(a)):
		a[j] *= num
	for j in range(len(a)):
		if 10 <= a[j] < 100:
			ten(a, j)
		if 100 <= a[j] < 1000:
			hundred(a, j)
print(sum(a))
