
T = int(raw_input())


for i in xrange(T):

	d = {}
	NN = int(raw_input())
	N = NN
	j = 0
	f = False
	while j<100000:
		for n in str(N):
			if n not in d:
				d[n] = 1


		if len(d) is 10:
			f = True
			break

		N += NN
		j += 1

	if f:
		print "Case #%d:"%(i+1), N
	else:
		print "Case #%d: INSOMNIA"%(i+1)
