def b_fun(check):
	if check % 4 == 0:
		if check % 100 == 0:
			if check % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	return False


year = 1901
sundays = 0
days = 2
months = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while year <= 2000:
	months[1] = 29 if b_fun(year) else 28
	i = 0
	while i < 12:
		if days == 7:
			sundays += 1
		days += months[i] % 7
		if days > 7:
			days -= 7
		i += 1
	year += 1
print(sundays)
