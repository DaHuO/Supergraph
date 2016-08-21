T = int(raw_input())

def solve():
	k, c, s = [int(x) for x in raw_input().split()]
	ans = (k + c - 1) / c
	if ans > s:
		print "IMPOSSIBLE"
		return
	a = []
	for i in range(ans):
		now = 0
		for j in range(i * c, (i + 1) * c):
			now *= k
			now += min(j, k - 1)
		a.append(now)
	print ' '.join([str(x + 1) for x in a])

for i in range(1, T + 1):
	print "Case #%d:" % i,
	solve()