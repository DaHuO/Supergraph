t = int(raw_input())

for i in xrange(1, t+1): 

	k,c,s = [int(s) for s in raw_input().split(" ")]
	ans = ""
	for j in range(1,s+1):
		ans = ans + " " + str(j)
	print "Case #{}: {}".format(i,ans)

