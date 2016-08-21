#!/usr/bin/python

import os
import sys
import string
import re


def process (text):

	s = ""

	lines = text.split("\n")
	while "" in lines:
		lines.remove("")

	N = None
	i = 1
	for line in lines:
		#print line
		if i == 0:
			pass
		elif i == 1:
			N = str(line)
		else:
			n = int(line)
			r = calc(n)
			s += "Case #%d: %s\n" % (i-1, r[1])
		i += 1

	return s


def calc (N):

	l = []
	i = 0
	n = None
	while True:
		i += 1
		n = i * N
		for j in str(n):
			j = int(j)
			if j not in l:
				l.append(j)
		#print "%d: %d: %s" % (i, n, str(l))
		if len(l) == 10:
			break
		if i>10000:
			n = "INSOMNIA"
			break

	n = str(n)

	return (i, n)


if __name__ == "__main__":

	( inputfile, ) = sys.argv[1:]

	inpt = """Input

5
0
1
2
11
1692"""

	inpt = open(inputfile, "r").read()
	outputfile = inputfile + ".out"
	out = process(inpt)
	outpt = open(outputfile, "w")
	outpt.write(out)
	outpt.close()

	#for i in (5, 0, 1, 2 , 11, 1692):
	#	print ">>>>>> %d" % i
	#	print calc(i)

