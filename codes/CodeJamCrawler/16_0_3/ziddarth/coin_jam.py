from collections import OrderedDict


def load_primes(limit=None):
	primes = OrderedDict()
	with open("C:\Dev\hackerrank\leetcode\primes.txt", 'r') as f:
		for p in f:
			p = int(p)
			if limit and p > limit:
				break
			primes[p] = True
	print 'Loaded %d primes' % len(primes)
	return primes


def main():
	size = 32
	start = (2 ** (size-1)) + 1
	end = (2 ** size)
	primes = load_primes()
	required_count = 500
	found = 0
	# for n in xrange(start, end, 2):
	while start < end:
		n = start
		base_2 = '{:b}'.format(n)

		result = [base_2]
		for i in range(2, 11):
			m = n
			if i > 2:
				m = sum(i ** index for index, k in enumerate(reversed(base_2)) if k == '1')
			if m in primes:
				break
			for j in primes.iterkeys():
				if m % j == 0:
					result.append(str(j))
					# result.append((m, j,))
					break
			else:
				# print 'FAILED to find divisor for', m
				break

		# no break
		else:
			found += 1
			# print base_2, result
			print ' '.join(result)
			if found == required_count:
				break
		start += 2

if __name__ == '__main__':
	main()