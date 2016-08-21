filename = 'B-large.in'
f = open(filename,'r')


T = int(f.readline())
for t in range(1,T+1):
	s = f.readline()
	if s[-1] == '\n':
		s = s[:-1]
	ans = (s[-1] == '-')
	for i in range(len(s)-1):
		if s[i] != s[i+1]:
			ans += 1
	print "Case #%d: %d" % (t,ans)