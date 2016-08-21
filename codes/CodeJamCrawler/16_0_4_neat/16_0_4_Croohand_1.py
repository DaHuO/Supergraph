t = int(input())
for test in range(t):
	print('Case #%s: ' % (test + 1), end = '')
	k, c, s = map(int, input().split())
	if k == 1:
		print(1)
	elif c == 1 and s < k:
		print('IMPOSSIBLE')
	elif c == 1:
		for i in range(k):
			print(i + 1, end = ' ')
		print()
	else:
		ans = []
		add = 2 * (k ** (c - 1)) + 2
		if k % 2:
			ans.append(k)
			k -= 1
		cur = 2
		for i in range(2, k + 1, 2):
			ans.append(cur)
			cur += add
		if (len(ans) > s):
			print('IMPOSSIBLE')
		else:
			for i in ans:
				print(i, end = ' ')
			print()
