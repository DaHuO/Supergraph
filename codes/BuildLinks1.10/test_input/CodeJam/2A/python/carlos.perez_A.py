def reorder(xs):
	if len(xs) == 1:
		return xs

	left = reorder(xs[:len(xs) / 2])
	right = reorder(xs[len(xs) / 2:])

	return min(left + right, right + left)

def solve(N, R, P, S):
	wins = {
		'P': 'PR',
		'R': 'RS',
		'S': 'PS'
	}

	solution = None
	for start in ['P', 'R', 'S']:
		xs = start

		for n in xrange(N):
			nextXs = []
			for x in xs:
				nextXs += wins[x]

			xs = nextXs

		r, s, p = 0, 0, 0
		for x in xs:
			if x == 'P': p += 1
			if x == 'R': r += 1
			if x == 'S': s += 1

		if r == R and s == S and p == P:
			xs = reorder(xs)

			if not solution or xs < solution:
				solution = xs

	return solution

for testCase in xrange(1, input() + 1):
	N, R, P, S = map(int, raw_input().split())

	solution = solve(N, R, P, S)
	print 'Case #{}: {}'.format(testCase, ''.join(solution) if solution else 'IMPOSSIBLE')