

if __name__ == "__main__":
	T = int(raw_input())
	test = 0
	while test < T:
		test += 1
		K, C, S = [int(i) for i in raw_input().split(" ")]
		if S < K:
			print "Case #%d: IMPOSSIBLE" % (test)
		else:
			if K == 1:
				print "Case #%d: 1" % (test)
			else:
				pos = [str(i) for i in xrange(1, K ** C + 1, K ** (C-1))]
				result = " ".join(pos)
				print "Case #%d: %s" % (test, result)