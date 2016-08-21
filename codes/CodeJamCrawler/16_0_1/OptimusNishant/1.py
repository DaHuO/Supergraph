for i in xrange(input()):
	s = raw_input()
	ans = s[0]
	s = s[1:]
	for ch in s:
		if ch >=ans[0]:
			ans =  ch + ans
		else:
			ans = ans + ch
	print "Case #{}: {}".format(i+1, ans)
