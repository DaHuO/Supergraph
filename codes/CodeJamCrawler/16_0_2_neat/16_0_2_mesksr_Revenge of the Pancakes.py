for t in xrange(int(raw_input())):
	s = raw_input()
	m = 0
	p = 1
	if (s[0] == '-'):
		m += 1
	else:
		p += 1
	for i in range(1, len(s)):
		if (s[i] != s[i-1]):
			if (s[i] == '-'):
				m += 2
			else:
				p += 2
	print "Case #"+str(t+1)+": "+str(min (m,p))
		
	
