import sys
from string import maketrans


d_plus = {}
d_minus = {}
t = maketrans('+-','-+')


def flip(s,i):
	return s[:i][::-1].translate(t) + s[i:]

def get_min_plus(s):
	min = 0

	if s in d_plus:
		return d_plus[s]

	if s[-1] == '+':
		min = get_min_plus(s[:-1])
	else:
		min = get_min_minus(s[:-1]) + 1

	for i in xrange(1,len(s)):
		t = get_min_plus(s[:i]) + get_min_minus(flip(s,len(s))[:len(s)-i]) + 2
		#print t ,s[:i], flip(s,len(s))[:len(s)-i]
		if t < min:
			min = t
	d_plus[s] = min
	return min

def get_min_minus(s):
	min = 0

	if s in d_minus:
		return d_minus[s]


	if s[-1] == '-':
		min = get_min_minus(s[:-1])
	else:
		min = get_min_plus(s[:-1]) + 1

	for i in xrange(1,len(s)):
		t = get_min_minus(s[:i]) + get_min_plus(flip(s,len(s))[:len(s)-i]) + 2
		#print t,s[:i], flip(s,len(s))[:len(s)-i]
		if t < min:
			min = t
	d_minus[s] = min
	return min

d_plus['+'] = 0
d_plus['-'] = 1

d_minus['+'] = 1
d_minus['-'] = 0

T = int(sys.stdin.readline())

for k in xrange(T):
	s = sys.stdin.readline()[:-1]
	#print s, flip(s,0)
	print "Case #{}: {}".format(k+1, get_min_plus(s))

