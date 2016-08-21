import fileinput
from itertools import product
from math import sqrt

def get_devisors(item):
	item = ''.join(item)
	devisors = []
	for base in xrange(2, 11):
		number = int(''.join(item), base)
		for i in xrange(2, int(sqrt(number))):
			if number % i == 0:
				devisors.append(i)
				break
	return devisors

if __name__ == '__main__':
	lines = fileinput.input()
	next(lines)
	for case, line in enumerate(lines):
		length, amount = tuple(map(int, line.strip().split(' ')))
		results = []
		for item in product(['0', '1'], repeat=length - 2):
			item = ['1'] + list(item) + ['1']
			divisors = get_devisors(item)
			if len(divisors) != 9:
				continue
			results.append((item, divisors))
			if len(results) >= amount:
				break
		print "Case #%d:" % (case + 1)
		for item, de in results:
			print ''.join(item), ' '.join(str(d) for d in de)


# 100011 5 13 147 31 43 1121 73 77 629
# 111111 21 26 105 1302 217 1032 513 13286 10101
# 111001 3 88 5 1938 7 208 3 20 11
