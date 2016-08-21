def solve(k,c,s):
	return ' '.join(map(str, range(1, k**c + 1, k**(c - 1))))

with open('output', 'w') as outputFile:
	with open('D-small.in','r') as inputFile:
		print inputFile.readline()
		count = 0
		for line in inputFile.readlines():
			k, c, s = map(int, line.split(' '))
			count += 1
			outputFile.write('Case #{0}: {1}\n'.format(count, solve(k, c, s)))