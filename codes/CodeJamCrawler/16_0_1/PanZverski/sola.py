def solve(n):
	f = [False]*10
	v = n
	c = 0
	while True:
		for ch in str(v):
			if not f[ord(ch) - ord('0')]:
				f[ord(ch) - ord('0')] = True
				c = c + 1
		if c == 10:
			break
		v = v + n
	return v

tests = input()
for test in range(1, tests + 1):
	n = input()
	ans = "INSOMNIA"
	if n != 0:
		ans = str(solve(n))
	print "Case #%d: %s" % (test, ans)
