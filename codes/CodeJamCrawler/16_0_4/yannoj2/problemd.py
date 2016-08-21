T = int(raw_input().strip())
for i in xrange(1,T+1):
	K,C,S = map(int, raw_input().strip().split())
	print "Case #" + str(i) + ": ",
	for i in xrange(1,K+1):
		print i,
	print