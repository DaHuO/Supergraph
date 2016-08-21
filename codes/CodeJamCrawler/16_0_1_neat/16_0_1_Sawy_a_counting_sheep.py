def problem_A():
	T = int(raw_input().strip()) + 1
	c = 0
	for t in range(1, T):
		seen_digits = set()
		seen_numbers = set()
		N = int(raw_input().strip())
		n = N
		c = t + 1
		slept = False
		factor = 1;
		while(True):
			if n in seen_numbers:
				break
			seen_numbers.add(n)
			strN = str(n)
			for ch in strN:
				seen_digits.add(ch)
			if len(seen_digits) == 10:
				slept = True
				break;
			factor = factor + 1
			n = factor * N
		print 'Case #{0}: {1}'.format(t, n if slept else 'INSOMNIA')