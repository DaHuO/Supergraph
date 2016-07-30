from sys import setrecursionlimit as slr
from collections import Counter
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

def gen(p, r, s):
	if p + r + s == 0:
		yield ''
	elif p + r + s == 1:
		yield 'P' if p else ('R' if r else 'S')
	else:
		if p > 0:
			for seq in gen(p-1, r, s):
				yield 'P' + seq
		if r > 0:
			for seq in gen(p, r-1, s):
				yield 'R' + seq
		if s > 0:
			for seq in gen(p, r, s-1):
				yield 'S' + seq

def winner(a, b):
	if a == b:
		raise ValueError()
	if a > b:
		a, b = b, a
	if a == 'P':
		if b == 'R':
			return 'P'
		if b == 'S':
			return 'S'
		assert False
	assert a == 'R' and b == 'S'
	return 'R'


def compete(seq):
	return ''.join(winner(a, b) for a,b in zip(seq[::2], seq[1::2]))

@memo
def works(seq):
	if len(seq) <= 1:
		return True
	try:
		return works(compete(seq))
	except ValueError:
		return False

def solve(n, r, p, s):
	for seq in gen(p, r, s):
		if works(seq):
			return seq
	return 'IMPOSSIBLE'

T, = get()
for caseNumber in range(1, T+1):
	put(caseNumber, solve(*get()))
