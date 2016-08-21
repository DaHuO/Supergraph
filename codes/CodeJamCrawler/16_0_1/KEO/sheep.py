
T = int(raw_input())

for i in xrange(1, T+1):
	print 'Case #{}:'.format(i),

	number = int(raw_input())

	counter = [0] * 10
	founded = 0

	i, j= 1, 1
	while founded < 10:
		for c in str(number * i):
			c = int(c)
			if not counter[c]:
				counter[c] = 1
				founded += 1
				j += 1

		i += 1

		if i - j > 10 ** 4:
			break

	if founded == 10: print number * (i-1)
	else: print 'INSOMNIA'
