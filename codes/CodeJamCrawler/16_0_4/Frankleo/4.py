t = int(raw_input())

for i in xrange(t):
	k, c, s = [int(x) for x in raw_input().split(' ')]
	res = ''
	for j in range(s):
		res += str(j+1) + ' '
	res.strip()
	print 'Case #%d: %s'%((i+1), res)
