#!/usr/bin/env python
from __future__ import division
import sys

def phoneNumber(s):

	count = dict()
	digits = list()
	for c in s:
		if c not in count:
			count[c] = 1
		else:
			count[c] += 1

	#Delete 0
	if "Z" in count:
		
		for n in range(count["Z"]):
			digits.append(0)
			count["Z"]-=1
			count["E"]-=1
			count["R"]-=1
			count["O"]-=1

	#Delete 2
	if "W" in count:
		
		for n in range(count["W"]):
			digits.append(2)
			count["T"]-=1
			count["W"]-=1
			count["O"]-=1

	#Delete 8
	if "G" in count:
		
		for n in range(count["G"]):
			digits.append(8)
			count["E"]-=1
			count["I"]-=1
			count["G"]-=1
			count["H"]-=1
			count["T"]-=1

	#Delete 4
	if "U" in count:
		
		for n in range(count["U"]):
			digits.append(4)
			count["F"]-=1
			count["O"]-=1
			count["U"]-=1
			count["R"]-=1

	#Delete 6
	if "X" in count:
		
		for n in range(count["X"]):
			digits.append(6)
			count["S"]-=1
			count["I"]-=1
			count["X"]-=1

	#Delete 7
	if "S" in count:
		
		for n in range(count["S"]):
			digits.append(7)
			count["S"]-=1
			count["E"]-=1
			count["V"]-=1
			count["E"]-=1
			count["N"]-=1

	#Delete 3
	if "H" in count:
		
		for n in range(count["H"]):
			digits.append(3)
			count["T"]-=1
			count["H"]-=1
			count["R"]-=1
			count["E"]-=1
			count["E"]-=1

	#Delete 5
	if "F" in count:
		
		for n in range(count["F"]):
			digits.append(5)
			count["F"]-=1
			count["I"]-=1
			count["V"]-=1
			count["E"]-=1

	#Delete 1
	if "O" in count:
		
		for n in range(count["O"]):
			digits.append(1)
			count["O"]-=1
			count["N"]-=1
			count["E"]-=1

	#Delete 9
	if "N" in count:
		
		for n in range(count["N"]//2):
			digits.append(9)
			count["N"]-=1
			count["I"]-=1
			count["N"]-=1
			count["E"]-=1
	
	#Return
	digits.sort()
	return "".join(str(n) for n in digits)


#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")
getstringlist = lambda : line().split(" ")
getint = lambda : int(line())
getintlist = lambda : [ int(n) for n in line().split(" ") ]


def main():

	#Number of test cases
	ntest = getint()

	#Cycle over test cases
	for t in range(ntest):
		
		s = line()

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,phoneNumber(s)))

if __name__=="__main__":
	main()