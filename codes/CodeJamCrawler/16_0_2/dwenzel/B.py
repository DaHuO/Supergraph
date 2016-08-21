def solve(input):
	while len(input) > 0 and input[-1] == '+':
		input = input[:-1]
	if len(input) == 0:
		return 0
	else:
		new_input = ''
		for c in input:
			if c == '+':
				new_input += '-'
			else:
				new_input += '+'
		return 1 + solve(new_input)

f = open('B-large.in', 'r')
lines = f.read().split('\n')
numCases = int(lines[0])
cases = lines[1:]
for i in range(numCases):
	print 'Case #' + str(i + 1) + ': ' + str(solve(cases[i]))