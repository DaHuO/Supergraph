#!/usr/bin/python

import sys
import array

f = open(sys.argv[1],'r')
t = int(f.readline())


for case in range(t):
	digitsarray = [0] * 10
	digitsseen = 0

	n = int(f.readline())
	current = n
	iteration = 1
	while(digitsseen < 10):
		while (current):
			digit = (int)(current%10)
			current = (int)(current/10)
			if (digitsarray[digit] == 0):
					digitsarray[digit] = 1
					digitsseen += 1
		iteration += 1
		current = n*iteration
		if (iteration > 100000000):
			break
	print ("Case #" + str(case+1) + ": ", end="")
	if (digitsseen == 10):
		print (current - n)
	else:
		print ("INSOMNIA")
