def getDigits(number):
	return [int(i) for i in str(number)]

def solve(case_number):
	number = int(raw_input())
	if (number == 0):
		print "Case #{}: {}".format(case_number, 'INSOMNIA')
	else:
		numbers = [i for i in range(10)]
		n = 1
		while numbers:
			digits = getDigits(number * n)
			for d in digits:
				if d in numbers:
					numbers.remove(d)
			n += 1
		print "Case #{}: {}".format(case_number, number * (n-1))

t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
	solve(case)