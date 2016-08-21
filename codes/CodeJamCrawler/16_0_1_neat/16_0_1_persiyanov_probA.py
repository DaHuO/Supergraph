import sys

lines = [line.strip() for line in sys.stdin]
T = int(lines[0])

for i in xrange(1, T+1):
	here = [False]*10
	N = int(lines[i])
	if N == 0:
		print "Case #{0}: INSOMNIA".format(i)
		continue
	else:
		cur = 0
		while not all(here):
			cur += N
			for d in str(cur):
				here[int(d)] = True
		print "Case #{0}: {1}".format(i, cur)