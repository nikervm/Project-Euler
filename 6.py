a = 0
for i in range(1, 101):
	a += i
a **= 2
for i in range(1, 101):
	a -= i ** 2
print(a)