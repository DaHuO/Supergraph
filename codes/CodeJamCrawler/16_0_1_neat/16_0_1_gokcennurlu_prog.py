import operator
T = int(raw_input())

for i in range(T):
	N = int(raw_input())
	if N == 0:
		print "Case #%d: INSOMNIA" % (i+1)
		continue
	else:
		c = 1
		bins = [0,0,0,0,0,0,0,0,0,0]
		origin = N
		while True:
			#print str(N)
			for digit in str(N):
				bins[int(digit)] += 1
			if reduce(operator.mul, bins, 1) != 0:
				print "Case #%d: %d" % (i+1, N)
				break
			else:
				N = origin*c
				c += 1