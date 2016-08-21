cases = input()

for c in xrange(1,cases+1):
	N = raw_input()
	tN = N
	
	digits = map(lambda x: str(x), range(10))
	
	i = 1
	while len(digits) > 0 and N != "0":
		N = str(int(tN) * i)
		for d in N:
			if d in digits:
				digits.remove(d)
		i += 1
	if N == "0":
		print "Case #%d: INSOMNIA" % c
	else:
		print "Case #%d: %s" % (c,N)