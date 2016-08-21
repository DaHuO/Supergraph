import sys

def solve(n):
	if n == 0:
		return 'INSOMNIA'

	i = 0
	seen = []
	while len(seen) < 10:
		i += 1
		s = set(str(i * n))
		for j in s:
			if j not in seen:
				seen.append(j)
	return i * n

cases = int(sys.stdin.readline().strip())

for case in xrange(cases):
	print 'Case #%d:' % (case + 1),
	print solve(int(sys.stdin.readline().strip()))
