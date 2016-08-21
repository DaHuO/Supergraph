def solve(N):
	if (N == 0):
		return 'INSOMNIA'
	total = 0
	seen = set()
	while(len(seen) != 10):
		total += N
		seen = seen.union(set(str(total)))
	return total


T = input()
for i in range(T):
	N = input()
	print 'Case #' + str(i + 1) + ': ' + str(solve(N))

