t = input()
for it in xrange(1,t+1):
	k,c,s = map(int,raw_input().split())
	print "Case #%d:" % it," ".join(map(str,range(1,s+1)))