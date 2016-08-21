#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(p):
    """Count the number of transitions from + to - and - to +, with an imaginary + added to the end
    """
    c = p[0] # current
    p = p[1:] + '+' #  pancake
    f = 0 # flip
    for i in p:
        if i != c:
            c = i
            f += 1
    return f

if __name__ == "__main__":
	for case in xrange(1, 1+input()):
		print "Case #{0}: {1}".format(case, solve(raw_input()))