from math import factorial

def solve(input):
	k, c, s = [int(i) for i in input.split(' ')]
	required_guesses = max(1, k - c + 1)
	if (s < required_guesses):
		return 'IMPOSSIBLE'
	start = 1
	offset = k - 2
	while c > 1:
		start *= k
		if offset > 0:
			start -= offset
			offset -= 1
		c -= 1

	solution = []
	for i in range(required_guesses):
		solution.append(str(start + i))
	return ' '.join(solution)

f = open('D-small-attempt0.in', 'r')
lines = f.read().split('\n')
numCases = int(lines[0])
cases = lines[1:]
for i in range(numCases):
	print 'Case #' + str(i + 1) + ': ' + str(solve(cases[i]))