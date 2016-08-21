import sys

def solve(s):
	y=''
	for x in s:
		if x + y < y + x:
			y = y + x
		else:
			y = x + y
	return y

T=int(sys.stdin.readline())
for i in xrange(1,T+1):
	s=sys.stdin.readline().strip()
	print('Case #%d: %s' % (i, solve(s)))