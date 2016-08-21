def calc(n, r, p, s):
	ans = ""
	if n == 1:
		if r != 0:
			ans += "R"
		if p != 0:
			ans += "P"
		if s != 0:
			ans += "S"
		if ans[1] < ans[0]:
			ans = ans[::-1]
	else:
		r1 = r / 2
		p1 = p / 2
		s1 = s / 2
		if r == p:
			r1 += 1
		elif p == s:
			p1 += 1
		else:
			s1 += 1
		ans1 = calc(n - 1, r1, p1, s1)
		ans2 = calc(n - 1, r - r1, p - p1, s - s1)
		if ans1 < ans2:
			ans = ans1 + ans2
		else:
			ans = ans2 + ans1
	return ans

T = int(raw_input())
for _ in range(1, 1 + T):
	print "Case #{}:".format(_),
	n, r, p, s = map(int, raw_input().split())
	m = 2 ** n
	if set([r, p, s]) - set([m / 3, m / 3 + 1]):
		print "IMPOSSIBLE"
	else:
		ans = calc(n, r, p, s)
		print ans