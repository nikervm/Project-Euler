a = "75 \
95 64 \
17 47 82 \
18 35 87 10 \
20 04 82 47 65 \
19 01 23 75 03 34 \
88 02 77 73 07 63 67 \
99 65 04 28 06 16 70 92 \
41 41 26 56 83 40 80 70 33 \
41 48 72 33 47 32 37 16 94 29 \
53 71 44 65 25 43 91 52 97 51 14 \
70 11 33 28 77 73 17 78 39 68 17 57 \
91 71 52 38 17 14 91 43 58 50 27 29 48 \
63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

# Перевод строки в массив интов
a = list(map(int, a.split(' ')))

# Создание двумерного массива интов
row = 1
i = 0
b = []
while i < len(a):
	b.append([])
	for j in range(row):
		b[row - 1].append(a[i + j])
	i += row
	row += 1

# Получение числа (не оптимальный вариант (перебор))
c = []


def fun(res, mas, iter_i, iter_j, size):
	if iter_i == size - 1:
		c.append(res + mas[iter_i][iter_j])
		return
	res += mas[iter_i][iter_j]
	fun(res, mas, iter_i + 1, iter_j + 1, size)
	fun(res, mas, iter_i + 1, iter_j, size)


fun(0, b, 0, 0, len(b))
print(max(c))
