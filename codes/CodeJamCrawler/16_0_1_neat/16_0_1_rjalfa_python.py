t = input()
for i in xrange(1,t+1):
	k = input()
	if k == 0:
		print "Case #%d: INSOMNIA" % i
		continue
	s = set([])
	l = k
	while len(s) < 10:
		s = s.union(set(list(str(l))))
		if len(s) == 10:
			break
		l += k
	print "Case #%d: %d" % (i,l)