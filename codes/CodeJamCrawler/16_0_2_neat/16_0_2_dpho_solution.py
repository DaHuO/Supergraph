for T in xrange(1, int(raw_input())+1):
	_s = raw_input()
	s = [_s[0]]
	for c in _s:
		if c != s[-1]:
			s.append(c)

	s = "".join(s)

	res = 2*s.count("-")
	if s[0] == "-": res -= 1
	print "Case #%d: %d" % (T, res)
