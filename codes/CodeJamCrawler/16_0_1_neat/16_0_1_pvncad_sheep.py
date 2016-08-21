import sys

T = int(sys.stdin.readline())

for testcase in xrange(1, T + 1):
	N = int(sys.stdin.readline())
	seen = set(str(N))
	
	if N == 0:
		print "Case #%d: INSOMNIA" % (testcase, )
		continue
	mult = 1
	while True:
		if len(seen) == 10:
			print "Case #%d: %d" % (testcase, mult * N)
			break
		mult += 1
		digits = list(str(mult * N))
		seen = seen.union(set(digits))
		
		