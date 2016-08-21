T = input()

for testCase in xrange(1, T + 1):
	N = input()

	numbers = [0] * 2501
	for _ in xrange(2*N - 1):
		for n in map(int, raw_input().split()):
			numbers[n] += 1

	missingNumbers = []
	for i in xrange(2501):
		if numbers[i] % 2 == 1:
			missingNumbers += [str(i)]

	print 'Case #{}: {}'.format(testCase, ' '.join(missingNumbers))
