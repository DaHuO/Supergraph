def print_ans(test, ans):
	if (ans[0] == -1):
		s = 'IMPOSSIBLE'
	else:
		s = ' '.join(map(str, ans))
	print 'Case #%d: %s' % (test, s)

T = int(raw_input())

for test in range(1, T + 1):
	K, C, S = map(int, raw_input().split())
	cnt = (K + (C - 1)) / C
	if (cnt > S):
		print_ans(test, [-1])
	else:
		ans = []
		for i in range(cnt):
			now = 0
			for j in range(0, C):
				if (i * C + j < K):
					now = now * K + (i * C + j)
				else:
					now = now * K
			ans.append(now + 1)
		print_ans(test, ans)

