
def solve(s):
	i, j = 0, len(s)
	l, r = "", ""
	while i < j:
		m = max(s)
		mi = s.rfind(m)
		l += m
		r = ''.join(s[mi+1:j]) + r
		j = mi
		s = s[i:j]
	return l + r

if __name__ == '__main__':
	t = int(raw_input())
	for i in xrange(t):
		print "Case #{}: {}".format(i + 1, solve(raw_input()))
