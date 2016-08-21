import codejam as gcj
gcj.load_input('A-large.in')

T = gcj.read_input('i')
for t in range(T):
	N = gcj.read_input('i')

	if N == 0:
		answer = 'INSOMNIA'
	else:
		digits = set()
		M = N
		while len(digits) < 10:
			answer = M
			digits.update(list(str(M)))
			M += N
		
	print 'Case #%i:' % (t + 1), answer

