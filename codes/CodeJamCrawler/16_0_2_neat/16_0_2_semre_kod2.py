

T = int(raw_input())


for i in xrange(T):

	N = raw_input().rstrip('+')

	region = 0

	ch = None

	for l in N:

		if ch != l:
			region += 1
			ch = l

	print "Case #%d:"%(i+1),region
