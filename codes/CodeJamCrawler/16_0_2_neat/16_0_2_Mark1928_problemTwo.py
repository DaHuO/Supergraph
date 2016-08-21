#!/bin/python

import sys

SAD = '-'
HAPPY = '+'

def flip(aString):
	res = ""
	for ch in aString[::-1]:
		if ch == SAD:
			res += HAPPY
		else:
			res += SAD
	return res

def flipinShit(x, flips):
	thing = x.find(SAD if x[0] == HAPPY else HAPPY)
	if thing == -1:
		if x[0] == SAD:
			flips += 1 
		return flips
	return flipinShit(flip(x[:thing]) + x[thing:], flips+1)

n = int(raw_input().strip())
for row in xrange(n):
	print "Case #" + str(row+1) + ": " + str(flipinShit(raw_input().strip(), 0))