#!/usr/bin/python

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	K, C, S = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

	solution = ""
	for j in xrange(1,K+1):
		solution += " " + str(j)

	print "Case #{}:{}".format(i, solution)
	# check out .format's specification for more formatting options


