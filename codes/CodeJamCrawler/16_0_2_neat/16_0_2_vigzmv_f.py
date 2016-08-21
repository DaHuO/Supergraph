for i in range(0,int(raw_input())):
	s = raw_input()
	
	l = s[len(s)::-1]
	start = 0
	last = '+'
	c = 0
	for x in range(0,len(l)):

		if l[x] == '-':
			start += 1

		if last == '+' and l[x] == '-' and start:
			c += 1
			last = '-'

		if last == '-' and l[x] == '+' and start:
			c += 1
			last = '+'

	print "Case #%d:" %i
	print c