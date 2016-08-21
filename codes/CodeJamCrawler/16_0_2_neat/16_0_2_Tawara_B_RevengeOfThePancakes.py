def solve():
	T = int(raw_input())
	for t in xrange(1,T+1):
		PC = [1 if s == "+" else 0 for s in raw_input()]
		cnt = 0
		N = len(PC)
		happy = 1; r = N-1
		for r in xrange(N-1,-1,-1):
			if PC[r] != happy:
				cnt += 1
				happy^= 1
		print "Case #%d: %d" % (t,cnt)

solve()