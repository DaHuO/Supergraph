#!/usr/bin/python2

t = int(raw_input())
for i in xrange(t):
	s = int(raw_input())
	if s == 0:
		print "Case #%d: INSOMNIA" % (i+1)
	else:
		count = []
		a = 1
		while len(count) < 10:
			b = list(str(a*s))
			for x in b:
				if not x in count:
					count.append(x)
			a += 1
		a -= 1
		print "Case #%d: %d" % (i+1,a*s)


