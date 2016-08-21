for t in range(input()):
	s = list(raw_input())
	c = 0
	for l in range(len(s)-1,-1,-1):
		if s[l] =='-':
			c += 1
			for x in range(l+1):
				if s[x]=='-': 
					s[x] = '+'
				else: 
					s[x] = '-'
		
	print "Case #" + str(t+1) + ": " + str(c)