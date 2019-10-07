ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def to_words(i):
	if 1 <= i < 20:
		return ones[i]
	elif 20 <= i < 100:
		return tens[i // 10] + (ones[i % 10] if (i % 10 != 0) else "")
	elif 100 <= i < 1000:
		return ones[i // 100] + "hundred" + ("and" + to_words(i % 100) if (i % 100 != 0) else "")


s = 0
for k in range(1, 1000):
	s += len(to_words(k))
print(s + 11)
