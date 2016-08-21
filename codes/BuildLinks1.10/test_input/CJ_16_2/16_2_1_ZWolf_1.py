import time
import math
import fractions
import numpy as np
from math import *
from fractions import *
from operator import itemgetter, attrgetter

start = time.time()

fname = "A-large"

ifile = open(fname + '.in', 'r')
ofile = open(fname + '.out', 'w+')

def minus (string, stmp):
	for i in stmp:
		index = string.index(i)
		string = string[:index] + string[index+1:]
	return string

def digit(string):
	s = []
	while string != "":
		if 'Z' in string:
			s.append("0")
			string = minus(string, "ZERO")
		elif 'W' in string:
			s.append("2")
			string = minus(string, "TWO")
		elif 'X' in string:
			s.append("6")
			string = minus(string, "SIX")
		elif 'G' in string:
			s.append("8")
			string = minus(string, "EIGHT")
		elif 'H' in string:
			s.append("3")
			string = minus(string, "THREE")
		elif 'R' in string:
			s.append("4")
			string = minus(string, "FOUR")
		elif 'F' in string:
			s.append("5")
			string = minus(string, "FIVE")
		elif 'V' in string:
			s.append("7")
			string = minus(string, "SEVEN")
		elif 'O' in string:
			s.append("1")
			string = minus(string, "ONE")
		else:
			s.append("9")
			string = minus(string, "NINE")

	s.sort()
	stmp = ""
	for i in s:
		stmp += i

	return stmp



############ main #############################	
with ifile:
	[num_case] = [int(x) for x in ifile.readline().split()] 

	for i in range(0, num_case):
		[string] = [str(x) for x in ifile.readline().split()]
		s = digit(string)

		# print "Case #%d: " + s % (num_case + 1)
		ofile.write("Case #%d: " % (i + 1))
		ofile.write(s + "\n" )






end = time.time()
print(end - start)



