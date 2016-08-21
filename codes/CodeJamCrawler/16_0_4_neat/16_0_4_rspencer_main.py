T = int(raw_input())
for t in xrange(1,T+1):
	print "Case #{:d}:".format(t),
	K,C,S = map(int,raw_input().split())
	print ' '.join(map(str,range(1,K+1)))
		
