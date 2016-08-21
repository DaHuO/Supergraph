def solve(s):
	dp = [0 for i in range(10)]
	dc = {}
	for c in s:
		if c == 'Z':
			dp[0] += 1
		elif c == 'W':
			dp[2] += 1
		elif c == 'U':
			dp[4] += 1
		elif c == 'X':
			dp[6] += 1
		elif c == 'G':
			dp[8] += 1
		if c in dc:
			dc[c] += 1
		else:
			dc[c] = 1
	if 'S' in dc:
		dp[7] = dc['S'] - dp[6]
	if 'F' in dc:
		dp[5] = dc['F'] - dp[4]
	if 'O' in dc:
		dp[1] = dc['O'] - dp[0] - dp[2] - dp[4]
	if 'N' in dc:
		dp[9] = (dc['N'] - dp[1] - dp[7])
		dp[9] /= 2
	if 'R' in dc:
		dp[3] = dc['R'] - dp[4] - dp[0]
	out = []
	for i in range(10):
		for j in range(dp[i]):
			out.append(i)
	return ''.join(map(str, out))
T = int(raw_input())
for i in range(1, T + 1):
	s = raw_input()
	print 'Case #%d: %s' % (i, solve(s))