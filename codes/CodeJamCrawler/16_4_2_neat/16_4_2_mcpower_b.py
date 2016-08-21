from math import factorial
from itertools import combinations
from functools import reduce

def binom(n, k):
	return factorial(n) // (factorial(k)*factorial(n-k))

def do(inp, left):
	if not inp:
		return 1
	new = inp[1:]
	if left:
		if left == len(inp):
			return reduce(lambda a, b: a*(1-b), inp, 1.0)
		return (1-inp[0]) * do(new, left-1) + inp[0] * do(new, left)
	return reduce(lambda a, b: a*b, inp, 1.0)

def do_case():
	n, k = map(int, input().split())
	inp = list(map(float, input().split()))
	out = 0.0
	for c in combinations(inp, k):
		out = max(out, do(c, k//2))
	return out


t = int(input())

for case in range(t):
	print("Case #{}:".format(case+1), do_case())
