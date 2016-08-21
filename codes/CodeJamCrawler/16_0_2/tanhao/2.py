f = open("2.in")
n = int(f.readline()[:-1])
for item, x in zip(range(1, n + 1), f.readlines()):
	x = x[:-1] + "+"
	ans = 0
	for i in xrange(len(x) - 1):
		if x[i] != x[i+1]:
			ans += 1
	print "Case #%d: %d" %(item, ans)
			
