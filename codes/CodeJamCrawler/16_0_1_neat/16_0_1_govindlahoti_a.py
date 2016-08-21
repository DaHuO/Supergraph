def ans(n):
	if n == 0:
		return 'INSOMNIA'
	m = 0
	s = set(range(10))
	while len(s)>0:
		m += n
		s = s - set([int(i) for i in str(m)])
	return m

for i in xrange(input()):
	n = input()
	print 'Case #{}: {}'.format(i+1, ans(n))