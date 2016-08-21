import itertools
#1 = G 
#0 = L


t = int(raw_input())
for i in xrange(1, t + 1):
	K, C, S = [int(s) for s in raw_input().split(" ")]
	print "Case #{}: {}".format(i, " ".join([str(n) for n in xrange(1, S + 1)]))
