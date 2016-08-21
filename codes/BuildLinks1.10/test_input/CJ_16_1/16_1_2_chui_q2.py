def solving(list):
	numbers = {}
	for line in list:
		hs = line.split(' ')
		for h in hs:
			if int(h) not in numbers:
				numbers[int(h)] = 0
			numbers[int(h)] += 1
	lost = []
	for k in numbers.keys():
		if numbers[k] % 2 == 1:
			lost.append(k)
	ret = [str(n) for n in sorted(lost)]
	return ret

with open('input', 'r') as input:
	test = [l.replace('\n', '') for l in input]
	n_case = int(test[0])
	n_rows = 0
	l = len(test)
	for case in range(n_case):
		N = int(test[1 + n_rows])
		start = 2 + n_rows
		n_rows += N*2
		print 'Case #%d: %s' % (case + 1, ' '.join(solving(test[start: n_rows + 1])))