T = int(raw_input())
for t in range(1, T + 1):
	x = map(int, raw_input().split())
	b, m = x[0], x[1]

	if (1 << (b - 2)) < m:
		print 'Case #%d: IMPOSSIBLE' % t
		continue

	o = [['0' for i in range(b)] for i in range(b)]

	for i in range(1, b):
		for j in range(i + 1, b):
			o[i][j] = '1'

	if m == (1 << (b - 2)):
		o[0][b-1] = '1'
		m -= 1
	z = b - 2
	while m != 0:
		if (m & 1) == 1:
			o[0][z] = '1'
		m >>= 1
		z -= 1
	print 'Case #%d: POSSIBLE' % t
	for i in range(b):
		print ''.join(o[i])
