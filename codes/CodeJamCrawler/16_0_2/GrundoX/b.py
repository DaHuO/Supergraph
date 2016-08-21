t = int(raw_input())
for i in xrange(t):
	ans = 0
	s = raw_input()
	if s[0] == '-':
		ans += 1
	for j in xrange(len(s)-1):
		if s[j] == '+' and s[j+1] == '-':
			ans += 2
	print "Case #%d: %d" % (i+1,ans)
