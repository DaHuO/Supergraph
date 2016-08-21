def test(number):
	if (number == 0):
		return "INSOMNIA"
	else:
		digits = [False for x in range(10)]
		i = 0
		while (not all(digits)):
			i = i + 1
			result = number * i
			for digit in str(result):
				digits[int(digit)] = True
		return result

with open("a-large.in") as input:
	# consume number of cases
	input.readline()
	# read in each test case
	i = 1
	for line in input:
		print("Case #" + str(i) + ": " + str(test(int(line))))
		i = i + 1
