num_cases = int(raw_input())

for case in xrange(1, num_cases + 1):
	n = int(raw_input())
	if n == 0:
		print "Case #{}: INSOMNIA".format(case)
		continue
	seen = set()
	now = n
	i = 0
	while len(seen) < 10:
		i += 1
		now = n * i
		seen.update(list(str(now)))

	print "Case #{}: {}".format(case, now)