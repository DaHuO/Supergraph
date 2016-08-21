#!/usr/bin/env python

def pancake(pancakes):
	n = 1
	for i in range(1,len(pancakes)):
		if pancakes[i] != pancakes[i-1]:
			n += 1
	return n -((n%2)^(pancakes[0]=='-'));

t = int(raw_input())  
for i in xrange(1, t + 1):
	print "Case #{}: {}".format(i, pancake(raw_input()))