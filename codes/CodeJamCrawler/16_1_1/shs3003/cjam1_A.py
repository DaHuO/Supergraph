T = int(raw_input())

for t in xrange(1,T+1):
	s = raw_input()
	cur_max = s[0]
	ans = "" + s[0]
	for i in range(1,len(s)):
		if s[i]>=cur_max:
			cur_max = s[i]
			ans = cur_max + ans
		else:
			ans += s[i]
		#print ans
		
	print "Case #{0}: {1}".format(t,ans)