
def find(org, times, new=None):
	if new is None: new = org

	if times == 1: return new

	new = new.replace('G', 'G'*len(org))
	new = new.replace('L', org)
	return find(org, times-1, new)


N = int(raw_input())



for c in xrange(1, N+1):
	print 'Case #{}:'.format(c),

	K, C, S = map(int, raw_input().split())

	if K == 1: print 1; continue

	if C == 1 and K <= S:
		print ' '.join(map(str, range(1, K+1)))

	elif C != 1 and K - 1 <= S:
		print ' '.join(map(str, range(2, K+1)))

	else:
		print 'IMPOSSIBLE'
