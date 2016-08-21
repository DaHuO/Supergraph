def solve():
	dgt = set(map(str,range(10)))
	T = int(raw_input())
	for t in xrange(T):
		N = int(raw_input())
		n = N
		if N == 0:
			print "Case #%d: INSOMNIA" % (t+1,)
		else:
			tmp_dgt = set(list(str(N)))
			while tmp_dgt != dgt:
				n += N
				tmp_dgt |= (set(list(str(n))))
			print "Case #%d: %d" % (t+1,n)
solve()