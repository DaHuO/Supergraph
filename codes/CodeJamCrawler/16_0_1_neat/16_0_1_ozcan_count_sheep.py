def count_sheep(n):
	if n== 0:
		return 'INSOMNIA'

	digits = range(10)
	x = 1
	while True:
		j = x * n
		while j > 0:
			column = j % 10
			digits[column] = -1
			j = j - column
			j = j / 10
		if (sum(digits) == -10):
			return x*n
		x += 1

t = int(raw_input())
for i in xrange(1, t + 1):
	n = int(raw_input())
	print "Case #{}: {}".format(i, count_sheep(n))