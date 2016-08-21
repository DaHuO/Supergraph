t = int(input())
j = 0
while j < t:
	j += 1
	n = int(input())
	if n == 0:
		print('Case #{}: {}'.format(j, 'INSOMNIA'))
	else:
		d = {}
		m = 0
		while len(d) < 10:
			m += n
			for k in str(m):
				d[k] = True
		print('Case #{}: {}'.format(j, m))