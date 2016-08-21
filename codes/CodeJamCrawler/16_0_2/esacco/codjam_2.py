def solve(s):
	if len(s) == 0:
		return 0
	else:
		flips = 0
		actual_c = s[0]
		for c in s[1:]:
			if c != actual_c:
				flips += 1
				actual_c = c
		if actual_c == '-':
			flips += 1
		return flips

with open('output', 'w') as outputFile:
	with open('B-large.in','r') as inputFile:
		print inputFile.readline()
		count = 0
		for line in inputFile.readlines():
			count += 1
			outputFile.write('Case #{0}: {1}\n'.format(count, solve(line.replace('\t', '').replace('\n',''))))