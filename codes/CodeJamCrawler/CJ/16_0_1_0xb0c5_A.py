def naive(n):
	if n == 0:
		return 'INSOMNIA'

	digits = set()
	
	count = 0
	while len(digits) < 10:
		count += 1
		for d in str(count * n):
			digits.add(d)
	return count * n


n_cases = input()

for case in range(1, n_cases+1):
	i = input()
	print 'Case #%d: %s' % (case, naive(i))
