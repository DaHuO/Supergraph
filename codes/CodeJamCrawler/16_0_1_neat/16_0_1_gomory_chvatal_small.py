def sheep(n):

	a = set([])
	ans = 'INSOMNIA'

	i = 1
	while i < 1000000:
		a.update( set( [x for x in str((n*i))] ))
		if len(a) == 10:
			ans = i*n
			break
		i += 1 
	
	return ans




file = open('A-large.in', 'r')

n = int(file.readline().strip())

for i in xrange(1, n+1):
	t = int(file.readline().strip())
	print 'Case #%d: %s' % (i, str(sheep(t)))
