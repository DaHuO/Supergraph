import collections

numbersInLetters = { 0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR',
	5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE' }
lettersInNumbers = { n: collections.Counter(l) for n, l in numbersInLetters.iteritems() }

for testCase in xrange(input()):
	letters = collections.Counter(raw_input())
	numbers = []

	for number in [0, 6, 8, 2, 7, 5, 9, 4, 3, 1]:
		lettersInNumber = lettersInNumbers[number]
		possible = True

		while possible:
			for k, v in lettersInNumber.iteritems():
				possible = letters.get(k, 0) >= v

				if not possible:
					break

			if possible:
				numbers += [str(number)]
				for k, v in lettersInNumber.iteritems():
					letters[k] -= v

	print 'Case #{}: {}'.format(testCase + 1, ''.join(sorted(numbers)))