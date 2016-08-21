T = int(raw_input())
for i in xrange(1, T+1):
	N = raw_input()
	nums = set(N)
	N = int(N)
	print "Case #%d:" % i,
	if(N == 0):
		print "INSOMNIA"
	else:
		j = 2
		while(len(nums) != 10):
			 n = N * j
			 j += 1
			 nums |= set(str(n))
		print n


