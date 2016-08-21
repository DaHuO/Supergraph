for test in range(1, int(input()) + 1):
	s = list(input())
	n = len(s)
	ans = 0
	for i in range(n - 1, -1, -1):
		if s[i] == '-':
			ans += 1
			for j in range(i + 1):
				if s[j] == '-': s[j] = '+'
				else: s[j] = '-'
	print("Case #%s: %s" % (test, str(ans)))
