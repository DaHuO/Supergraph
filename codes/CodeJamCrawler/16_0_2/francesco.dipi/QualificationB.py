#!/usr/bin/python

T = int(raw_input())

def solve(s):
	return s.count("+-") * 2 + int(s[0] == "-")

for t in xrange(T):
	
	S = raw_input()
	
	print "Case #%d: %d" % (t+1, solve(S))

