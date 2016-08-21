#!/usr/bin/python

T = int(raw_input())

def solve(x):
	s = set()
	for i in xrange(1,10000):
		for c in str(i*int(x)):
			s.add(c)
		if len(s) == 10:
			return str(i*int(x))
	return "INSOMNIA"


for t in xrange(T):
	
	N = raw_input()
	
	print "Case #%d: %s" % (t+1, solve(N))
