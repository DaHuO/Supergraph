def check(a):
	l = len(a)
	f = [[0] * 402 for x in a]
	f[0][l + 1] = a[0]
	f[0][l - 1] = 1 - a[0]
	for i in range(l - 1):
		for j in range(2 * l + 1):
			if j != 0:
				f[i + 1][j - 1] += f[i][j] * (1 - a[i + 1])
			f[i + 1][j + 1] += f[i][j] * a[i + 1]
	return f[l - 1][l]

T = int(raw_input())
for _ in range(1, T + 1):
	print "Case #{}:".format(_),
	n, k = map(int, raw_input().split())
	a = sorted(map(float, raw_input().split()))
	ans = check(a[:k])
	for i in range(1, k + 1):
		res = check(a[: (k - i)] + a[-i: ])
		ans = max(ans, res)
	print ans