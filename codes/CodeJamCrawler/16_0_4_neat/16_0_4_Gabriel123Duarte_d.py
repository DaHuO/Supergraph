caso = 1
t = input()
for T in xrange(1, t + 1):
	k, c, s = raw_input().split()
	k = int(k)
	c = int(c)
	s = int(s)

	p = k ** c
	if p == 2 and s == 1:
		print "Case #" + str(T) + ": IMPOSSIBLE"
	else:
		if p == 2:			
			print "Case #" + str(T) + ": 1 2"
		else:
			print "Case #" + str(T) + ":",
			for i in xrange(1, s + 1):
				print str(i),
			print ""

#print total


