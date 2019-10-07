# Первый способ (простой)
n, num, res = 1000, 2, 1
for i in range(n):
	res *= num
res = list(str(res))
for i in range(len(res)):
	res[i] = int(res[i])
print(sum(res))

# Второй способ
n, num, a = 1000, 2, [1]
for i in range(n):
	for j in range(len(a)):
		a[j] *= num
	for j in range(len(a)):
		if a[j] >= 10:
			if j == len(a) - 1:
				a.append(1)
				a[j] -= 10
				break
			a[j] -= 10
			a[j + 1] += 1
print(sum(a))
