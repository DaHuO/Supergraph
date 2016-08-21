#!/usr/bin/env python

def sheep(n):
	seen = [0]*10
	if n==0: return 'INSOMNIA'
	curn = 0
	while sum(seen)!=10:
		curn += n
		k = curn
		while k!=0:
			seen[k%10] = 1
			k = k/10
	return curn;

t = int(raw_input())  
for i in xrange(1, t + 1):
	n = int(raw_input())
	print "Case #{}: {}".format(i, sheep(n))