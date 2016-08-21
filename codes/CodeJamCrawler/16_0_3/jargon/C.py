from itertools import chain
from itertools import combinations as C
#from math import ceil
#from math import sqrt

# All we need :)
DIVISORS = (2, 3, 7)

# Generate something guaranteed to be divisible by 3. :-)
def gen3(N):
	def from_tuple(t, x):
		y = '0' if x == '1' else '1'
		p = 0
		s = '1'
		for i in t:
			s += y * (i - p) + x
			p = i + 1
		s += y * (N - 1 - len(s)) + '1'
		return s
	def from_tuples(t, x):
		for i in t:
			yield from_tuple(i, x)
	strs = []
	for i in xrange(1, N - 1, 3):
		if i <= N / 2 - 1:
			strs = chain(strs, from_tuples(C(xrange(N - 2), i), '1'))
		else:
			strs = chain(strs, from_tuples(C(xrange(N - 2), N - 2 - i), '0'))
	return strs

def find_factor(n):
	#for i in xrange(2, int(ceil(sqrt(n)))):
	for i in DIVISORS:
		if n % i == 0:
			return i
	return None

def check(s):
	x = []
	for i in xrange(2, 11):
		f = find_factor(int(s, i))
		if not f:
			return 0
		x.append(f)
	print s, ' '.join(map(str, x))
	return 1

def solve(t, N, J):
	found = 0
	print 'Case #%d:' % t
	for s in gen3(N):
		found += check(s)
		if found == J:
			return

def main():
	for t in xrange(1, 1 + int(raw_input())):
		solve(t, *map(int, raw_input().split()))

if __name__ == '__main__':
	main()
