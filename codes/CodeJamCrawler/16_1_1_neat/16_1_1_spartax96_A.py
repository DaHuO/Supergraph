t = input()
for _ in xrange(t):
	s = raw_input()
	r = s[0]
	for i in s[1:]:
		if ord(i) >= ord(r[0]):
			r = i + r
		else:
			r = r + i
	print "Case #%d: %s" % (_+1, r)