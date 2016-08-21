import sys
T = int(sys.stdin.readline())
for i in range(T):
	N = int(sys.stdin.readline())
	digit_set = set()
	count = 1
	if N > 0:
		while len(digit_set) < 10:
			digit_set = digit_set.union(set(str(N*count)))
			count += 1
		answer = str(N*(count-1))
	else:
		answer = "INSOMNIA"
	print "Case #%d: %s" % (i+1, answer)
