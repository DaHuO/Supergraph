#!/usr/bin/env python

nc = int(raw_input())

for i in xrange(1, nc + 1):
	stack = list(raw_input())
	
	n_it = 0

	till_n = 0
	while (stack.count("+") != len(stack)):
		for j in xrange(1, len(stack)):
			if stack[j] != stack[j-1]:
				till_n = j
				break
		if stack.count("-") == len(stack):
			till_n = len(stack) 

		n_it += 1
		for j in xrange(0, till_n):
			stack[j] = "+" if stack[j] != "+" else "-"
			
	print "Case #{}: {}".format(i, n_it)
	

