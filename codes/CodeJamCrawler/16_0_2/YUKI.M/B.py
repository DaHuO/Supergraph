t = input()
for tt in range(t):
	s = raw_input()
	ans = 0

	for i in range(len(s) - 1):
		if s[i + 1] != s[i]:
			ans += 1

	if s[-1] == "-":
		ans += 1

	print "Case #%d: %d" % (tt + 1, ans)
