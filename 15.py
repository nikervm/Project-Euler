a = []
x = 20
y = 20
for i in range(x + 1):
	a.append([])
	for j in range(y + 1):
		if j == 0 or i == 0:
			a[i].append(1)
		else:
			a[i].append(a[i][j - 1] + a[i - 1][j])
print(a[x][y])
