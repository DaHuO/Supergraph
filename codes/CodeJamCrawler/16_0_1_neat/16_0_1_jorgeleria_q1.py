def solve(n):
	if n == 0:
		return 'INSOMNIA'
	numbers = [1,1,1,1,1,1,1,1,1,1]
	i = 0
	while sum(numbers) > 0:
		i += 1
		digits = map(int, list(set(str(n*i))))
		for digit in digits:
			numbers[digit] = 0
	return str(i*n)


lines = map(int, open('in2.in','r').readlines()[1:])
for i, line in enumerate(lines):
	print 'Case #%i: %s' % (i+1, solve(line))
