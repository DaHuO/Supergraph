def get_digits(n):
	ret = []
	while n > 0:
		ret.append(n%10)
		n = n//10
	return ret

def testcase(n):
	if n is 0:
		return 'INSOMNIA'
	coeff = 1
	count = 0
	seen = [False] * 10
	while count < 10:
		temp = get_digits(coeff * n)
		for digit in temp:
			if seen[digit] is False:
				count = count + 1
				seen[digit] = True
		if count is 10:
			break
		coeff = coeff + 1
	return coeff * n

input = open('A-large.in', 'r')
output = open('A-large-output.out', 'w')
T = int(input.readline())

for i in range(T):
	inp = int(input.readline())
	out = 'Case #' + str(i + 1) + ': ' + str(testcase(inp)) + '\n'
	output.write(out)