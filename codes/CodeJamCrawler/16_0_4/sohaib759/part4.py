

t = int(raw_input())

for i in xrange(1, t + 1):
	n, m, p = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

	print "Case #{}:".format(i),

	for x in range(1, p+1):
		if x == p:
			print x
		else:
			print x,

	