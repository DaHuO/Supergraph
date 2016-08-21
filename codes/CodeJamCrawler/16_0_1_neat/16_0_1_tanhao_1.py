f = open("1.in")
n = int(f.readline()[:-1])
a = [int(x[:-1]) for x in f.readlines()]
answer = set([str(x) for x in xrange(10)])
for item, x in zip(range(1, len(a) + 1), a):
	s = set()
	for i in xrange(1, 1000):
		tmp = x * i
		s = s.union( set(str(tmp)) )
		#print tmp, s
		if s == answer:
			print "Case #%d: %d" %(item, tmp)
			break
	else:
		print "Case #%d: INSOMNIA" %(item)
