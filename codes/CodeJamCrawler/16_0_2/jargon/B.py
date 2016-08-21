for t in xrange(1, int(raw_input()) + 1):
	f = 0
	for ch in raw_input()[::-1]:
		f += int('+-'.find(ch) != f % 2)
	print 'Case #%d: %d' % (t, f)
