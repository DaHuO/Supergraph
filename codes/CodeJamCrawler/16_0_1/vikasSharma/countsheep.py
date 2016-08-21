for tc in xrange(int(raw_input())):
	N = int(raw_input())
#	for m in xrange(0,1000001):
#		N = m
	if N == 0:
		print "Case #%d: INSOMNIA" %(tc+1)
	else:
		x = 1
		z = set()
		while(x):
			for i in list(str(N*x)):
				z.add(i)
			if len(z) == 10:
				print "Case #%d: %d" %(tc+1, N*x)
				break
			x+=1
