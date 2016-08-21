T = int(raw_input())

for t in range(1, T+1):
	s = raw_input()
	l_ = []
	l__ = []
	c = ''
	for i in range(len(s)):
		if(i == 0):
			c = s[0]
			l_.append(c)
		else:
			for x in l_:
				l__.append(x + s[i])
				l__.append(s[i] + x)
			l_ = l__
			l__ = []
	print "CASE #" + str(t) + ": " + sorted(l_)[len(l_) - 1]
				
				
		
			


