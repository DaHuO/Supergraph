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
	n, m = map(int, raw_input().split())
	for i in range(1<<(n-2)):
		x = (1<<(n-1)) + (i<<1) + 1
		y = [small(x, j) for j in range(2, 11)]
		if (min(y) > 0):
			print bin(x)[2:], y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8] 
			m -= 1
		if(m==0):
			break
	return

for case in range(T):
	print 'Case #' + str(case + 1) + ':'
	solve()
