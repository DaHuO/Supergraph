def findAnswer(n):
	if (n == 0):
		return 'INSOMNIA'

	endSet = set('1234567890')
	s = set()

	i = 1
	while True:
		s = s.union(set(str(i*n)))

		if (s == endSet):
			break

		i += 1
	return i*n

inlist = []
inf = open('A-large.in','r')
outf = open('output', 'w')
i = 1
skip = True
for line in inf:
	if skip:
		skip = False
		continue
	n = int(line)
	output = 'Case #' + str(i) + ': ' + str(findAnswer(n)) + '\n'
	outf.write(output)
	i += 1
print('done')
