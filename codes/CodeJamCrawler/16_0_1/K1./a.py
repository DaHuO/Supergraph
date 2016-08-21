

def getDigits(number):
	str_number = str(number)
	digit_set = set([])
	for digit in str_number:
		digit_set.add(digit)
	return digit_set


def getLastNumberBeforeSleep(number):
	if not number:
		return "INSOMNIA"
	else:
		digit_set = set([])
		i = 1
		last_number = 0
		while len(digit_set) != 10:
			last_number = number * i
			digit_set = digit_set | getDigits(last_number)
			i += 1
		return str(last_number)


n = int(input())
for i in range(n):
	number = int(input())
	result = getLastNumberBeforeSleep(number)
	print("Case #{}: {}".format(i+1, result))
	pass

