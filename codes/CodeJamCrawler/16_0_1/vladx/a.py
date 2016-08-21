import sys

def solve(n):
	m = [False]*10
	for i in xrange(1, 5000001):
		s = str(i*n)
		for c in s:
			m[ord(c)-ord('0')]=True
		if sum(m)==10:
			return s
	return 'INSOMNIA'

T = int(sys.stdin.readline())
for i in xrange(1,T+1):
	N = int(sys.stdin.readline())
	print('Case #%d: %s' % (i, solve(N)))