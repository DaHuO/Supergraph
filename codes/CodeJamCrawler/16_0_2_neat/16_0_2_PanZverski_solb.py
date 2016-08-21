def solve(s):
	cnt = 0
	for i in range(1, len(s)):
		if s[i - 1] != s[i]:
			cnt = cnt + 1
	if s[len(s) - 1] == '-':
			cnt = cnt + 1
	return cnt

tests = input()
for test in range(1, tests + 1):
	s = raw_input()
	ans = str(solve(s))
	print "Case #%d: %s" % (test, ans)
