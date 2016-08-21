def count_sheep(base):
	seen_digits = set()
	if base == 0:
		return 'INSOMNIA'
	curr = base
	while len(seen_digits) < 10:
		for digit in str(curr):
			seen_digits.add(digit)
		curr += base
	return curr - base


with open('A-large.in', 'rb') as inf, \
	 open('A-large.out', 'wb') as outf:
	t = int(inf.readline())
	for case_num in xrange(1, t+1):
		n = int(inf.readline())
		outf.write('Case #{0}: {1}\n'.format(case_num, 
						count_sheep(n)))