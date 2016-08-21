def f(n):
	if n == 0:
		return 'INSOMNIA'
	digs = set(str(n))
	i = 1
	while True:
		if len(digs) == 10:
			return str(n*i)
		i += 1
		digs |= set(str(n*i))

t = int(raw_input().strip())
for i in xrange(1, t+1):
	n = int(raw_input().strip())
	print 'Case #{}: {}'.format(i, f(n))