file = open('counting_sheep.txt', 'r')
output = open('counting_sheep_out.txt', 'w')

t = int(file.readline())
for i in xrange(0, t):
	n = file.readline()
	if int(n) == 0:
		output.write('Case #' + str(i + 1) + ': INSOMNIA\n')
		continue

	s = set()
	const = int(n)
	while True:
		for j in n:
			if j != '\n':
				s.add(j)
		if len(s) == 10:
			break
		else:
			n = str(int(n) + const)
	output.write('Case #' + str(i + 1) + ': ' + n + '\n')

file.close()
output.close()