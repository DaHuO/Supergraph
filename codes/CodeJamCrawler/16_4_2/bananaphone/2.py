T = int(raw_input())

import itertools
def factorial(n):
	if n == 0:
		return 1
	return n*factorial(n-1)

def binom(a, b):
	return (factorial(a)/factorial(b))/factorial(a-b)

def product(x):
	curr = 1
	for v in x:
		curr *= v
	return curr

d = {((), i) : 1}
def elem(seq, i):
	if (seq, i) in d:
		return d[(seq, i)]
	if i == 0:
		return 1
	if len(seq) == i:
		return product(seq)
	if i == 1:
		return sum(seq)
	out = elem(seq[:-1], i) + seq[-1]*elem(seq[:-1], i-1)
	d[(seq, i)] = out
	return out

def value(seq, K):
	out = 0
	for i in xrange(K/2, K+1):
		out += (-1)**(K/2 - i) * elem(seq, i) * binom(i, K/2)
	return out

def doprob():
	read = raw_input().split()
	N = int(read[0])
	K = int(read[1])
	read = raw_input().split()
	read = [float(x) for x in read]
	out = 0
	for i in itertools.combinations(read, K):
		if value(i, K) > out:
			out = value(i, K)

	return out

for qq in xrange(T):
	print "Case #" + str(qq+1) + ": " + str(doprob())