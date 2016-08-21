t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
	n = int(raw_input())
	N = n

	s = set(list(str(N)))

	while len(s) < 10:
		if (N == N+n):
			N = "INSOMNIA"
			break
		N += n
		s = s.union(set(list(str(N))))

	print "Case #{}: {}".format(i, N)
