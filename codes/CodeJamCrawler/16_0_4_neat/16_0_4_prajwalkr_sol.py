t = input()
for case in xrange(t):
	k,c,s = map(int, raw_input().split())
	print "Case #{}: {}".format(case + 1,' '.join([str(i + 1) for i in range(k)]))
