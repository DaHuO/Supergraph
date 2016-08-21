from sys import setrecursionlimit as slr
slr(10**9)

def memo(f):
	cache = dict()
	def wrap(*args):
		if args not in cache: cache[args] = f(*args)
		return cache[args]
	return wrap

getl = lambda: raw_input().strip().split()
get = lambda: map(int, getl())

def put(caseNumber, result):
	print "Case #%d: %s" % (caseNumber, result)

def solve(n, k, p):
	options = []
	for i in range(2**n):
		count = 0
		l = []
		for j, x in enumerate(p):
			if i & (1 << j):
				l.append(x)
		if len(l) == k:
			options.append(l)
	
	assert options

	return max(prob(o) for o in options)

def prob(p):
	@memo
	def pr(i, n):
		if abs(n) > i:
			return 0.0
		if i == 0:
			return 1.0
		return p[i-1] * pr(i-1, n+1) + (1.0 - p[i-1]) * pr(i-1, n-1)
	return pr(len(p), 0)

T, = get()
for caseNumber in range(1, T+1):
	put(caseNumber, solve(*(get() + [map(float, getl())])))

