ALL_DIGITS = set([x for x in range(10)])

def numbers(N):
	return set(int(x) for x in str(N))

def solve(N):
	if N == 0:
		return "INSOMNIA"
	seen = numbers(N)
	i = 2
	while seen != ALL_DIGITS:
		M = i*N
		seen = seen.union(numbers(M))
		i += 1
	return M

T = int(input())

for case in range(1, T+1):
	N = int(input())
	print("Case #%i: %s" % (case, solve(N)))