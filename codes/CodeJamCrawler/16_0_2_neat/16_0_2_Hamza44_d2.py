t = int (raw_input())
for i in xrange(1,t+1):
	counter = 0
	n = raw_input()
	for x in xrange(len(n)-1, -1,-1):
		if x is len(n) - 1 and n[x] is "-":
			counter += 1
		elif n[x] is "-" and n[x+1] is "+":
			counter += 1
		if counter > 0 and n[x] is "+" and n[x+1] is "-":
			counter += 1
	print "Case #{}: {}".format(i, counter)