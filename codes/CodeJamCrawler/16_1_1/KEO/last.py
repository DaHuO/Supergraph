

T = int(raw_input())
for t in xrange(1, T+1):
	print 'Case #{}:'.format(t),

	word = raw_input().strip()
	ans = word[0]

	for i in word[1:]:
		if i >= ans[0]:
			ans = i + ans
		else:
			ans += i

	print ans
