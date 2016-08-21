import sys

def f2(S):
	c = S[0]
	i = 1
	while i < len(S):
		if S[i] >= c[0]:
			c = S[i] + c
		else:
			c = c + S[i]
		i += 1
	return c

f = open(sys.argv[1], 'r')
N = int(f.readline().strip())
for case in xrange(1, N+1):
	s = f.readline().strip()
	output = f2(s)
	print 'Case #%s: %s' %(case, output)
