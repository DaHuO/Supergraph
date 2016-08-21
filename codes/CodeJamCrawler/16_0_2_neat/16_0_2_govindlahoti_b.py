def ans(a, c):
	i = len(a)-1
	while i>=0:
		if a[i] != c:
			break
		i-=1
	if i == -1:
		return 0
	else:
		if c == '+':
			d = '-'
		else:
			d = '+'
		return 1 + ans(a[:i+1], d)



for t in xrange(1, input() + 1):
	a = raw_input()
	print 'Case #{}: {}'.format(t, ans(a, '+'))