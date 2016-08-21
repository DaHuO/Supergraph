n = []
t = input()
for _ in xrange(t):
	#print t	
	n.append(raw_input())
c = 1
for i in n:
	opt = 0
	last_added = 0
	last_seen = i[0]
	for ch in i[1:]:
		if last_seen != ch:
			#print last_seen
			if last_seen == '-' and last_added != 2:
				opt += 1
				last_added = 1
			elif last_seen == '+':
				opt += 2
				last_added = 2
			last_seen = ch
	if  last_seen == '-' and opt == 0:
		print "Case #" + str(c) + ": " + str(1)
	else:
		print "Case #" + str(c) + ": " + str(opt)
	c += 1
