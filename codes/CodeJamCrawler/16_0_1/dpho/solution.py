for T in xrange(1, int(raw_input())+1):
	n = int(raw_input())

	if n == 0:
		print "Case #%d: %s" % (T, "INSOMNIA")
	else:
		res = n
		seen = set(list(str(n)))
		while len(seen) != 10:
			res += n
			for c in str(res):
				seen.add(c)

		print "Case #%d: %d" % (T, res)
