T = int(raw_input())


def small(n, k):

	r = 0
	x = 1
	for i in range(16):
		r += (n & 1) * x
		x *= k
		n >>= 1
	i = 2
	while (i * i <= r and i < 50):
		if(r % i == 0):
			return i
		i += 1
	return 0


def solve():
	K, C, S = map(int, raw_input().split())
	if(C * S < K):
		print 'IMPOSSIBLE'
		return
	l = 0
	while (l < K):
		r = 0
		for i in range(l, l+C):
			r = r * K + min(i, K-1)
		l += C
		if(l < K):
			print r+1,
		else:
		 	print r+1

for case in range(T):
	print 'Case #' + str(case + 1) + ':', 
	solve()
