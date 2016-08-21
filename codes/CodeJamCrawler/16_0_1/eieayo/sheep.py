def check_digit(x, digits):
	if x in digits:
		digits.remove(x)
	return digits

def sheep(n):
	i = 1
	digits = range(0,10)
	while len(digits) > 0:
		y = i*n
		counts = [int(x) for x in list(str(y))]
		for count in counts:
			check_digit(count, digits)
		i += 1
		z = i*n
		if y == z:
			return 'INSOMNIA'
	return y

def read_input(filename):
	f = open(filename, 'r')
	test_cases = []
	for line in f:
		test_cases.append(line)
	return test_cases


if __name__ == "__main__":
	f = open('output_large.txt', 'w')

	test_cases = read_input('A-large.in')
	num_cases = int(test_cases.pop(0))
	for x in range(0,num_cases):
		f.write("Case #{0}: {1}\n".format(x+1, sheep(int(test_cases[x]))))


