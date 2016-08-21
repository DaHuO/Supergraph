for x in xrange(int(raw_input())):
	k,c,s = map(int,raw_input().split())
	print 'Case #'+str(x+1)+':',
	coeff = []
	for i in range(c):
		coeff.append(pow(k,i))
	for i in range(s):
		ans = 1
		for j in coeff:
			ans += j*i
		print ans,
	print 