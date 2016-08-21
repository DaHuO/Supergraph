def score(xs, idx, yes, no):
	if yes == len(xs) / 2:
		ret = 1
		for x in xs[idx:]:
			ret *= (1 - x)

		return ret

	if no == len(xs) / 2:
		ret = 1
		for x in xs[idx:]:
			ret *= x

		return ret

	ret = xs[idx] * score(xs, idx + 1, yes + 1, no) + (1 - xs[idx]) * score(xs, idx + 1, yes, no + 1)

	return ret

def bruteforce(xs, idx, K, current):
	if K == 0:
		return score(current, 0, 0, 0)

	if K == len(xs[idx:]):
		return bruteforce(xs, idx + 1, K - 1, current + [xs[idx]])

	s1 = bruteforce(xs, idx + 1, K - 1, current + [xs[idx]])
	s2 = bruteforce(xs, idx + 1, K, current)
	return max(s1, s2)

for testCase in xrange(1, input() + 1):
	N, K = map(int, raw_input().split())
	xs = map(float, raw_input().split())

	solution = bruteforce(xs, 0, K, [])

	print 'Case #{}: {}'.format(testCase, solution)