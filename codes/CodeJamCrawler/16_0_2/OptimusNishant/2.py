t = input()
for i in xrange(t):
	s = raw_input()
	ans = 0
	l = len(s)
	for j in xrange(l-1):
		if s[j]!=s[j+1]:
			ans+=1
	if s[l-1]=="-":
		ans+=1
	print "Case #{}: {}".format(i+1,ans)
