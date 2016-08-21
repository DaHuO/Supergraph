def solve(input):
	input = int(input)
	if input == 0:
		return 'INSOMNIA'
	digits = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	x = 0
	while len(digits) > 0:
		x += input
		tmp = x
		while tmp > 0:
			if tmp % 10 in digits:
				digits.remove(tmp % 10)
			tmp /= 10
	return str(x)


f = open('A-large.in', 'r')
lines = f.read().split('\n')
numCases = int(lines[0])
cases = lines[1:]
for i in range(numCases):
	print 'Case #' + str(i + 1) + ': ' + solve(cases[i])