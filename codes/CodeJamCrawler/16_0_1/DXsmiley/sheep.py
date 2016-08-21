T = int(input())
for t in range(1, T + 1):
	n = int(input())
	if n == 0:
		print('Case #{}: INSOMNIA'.format(t))
	else:
		s = set()
		i = 0
		f = n
		while len(s) < 10:
			i += 1
			f = i * n
			for c in str(f):
				s.add(c)
		print('Case #{}: {}'.format(t, f))