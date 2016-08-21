def solve(n):
	if n == 0:
		return 'INSOMNIA'
	setOfDigits = set(c for c in str(n))
	mul = 1
	while len(setOfDigits) < 10:
		mul += 1
		setOfDigits = setOfDigits.union(set(c for c in str(n * mul)))
	return mul * n


with open('output', 'w') as outputFile:
	with open('A-large.in','r') as inputFile:
		print inputFile.readline()
		count = 0
		for line in inputFile.readlines():
			count += 1
			outputFile.write('Case #{0}: {1}\n'.format(count, solve(int(line))))