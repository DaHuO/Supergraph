def memo(f):
	cache = {}
	def memoized(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return memoized

@memo
def solve(pancakes):
	if len(pancakes) == 1:
		if pancakes[0] == '-':
			return 1
		return 0
	if pancakes[0] == pancakes[1]:
		return solve(pancakes[1:])
	return solve(pancakes[1:]) + 1

f = open('B.large.in', 'r')
out = open('B.large.out', 'w')

N = int(f.readline())

for i in xrange(N):
	pancakes = tuple(f.readline().strip('\n'))
	out.write('Case #{0}: {1}\n'.format(i + 1, solve(pancakes)))

f.close()
out.close()