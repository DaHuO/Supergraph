import sys
T = int(sys.stdin.readline())

for testcase in xrange(1, T + 1):
	K, C, S = [int(w) for w in sys.stdin.readline().split()]
	print "Case #%d: %s" % (testcase, " ".join(map(str, range(1, S + 1))))
