#!/usr/bin/env python
import random

def containremove(S, sub):
	nums = []
	Sr = S[:]
	for c in sub:
		num = Sr.find(c)
		if num == -1:
			return False, S
		else:
			Sr = Sr[:num] + Sr[num+1:]
			#print Sr
			nums.append(num)

	return True, Sr
				

def solve_case(S):


	while True:
		nums = {
			"ZERO": 0,
			"ONE": 0,
			"TWO": 0,
			"THREE": 0,
			"FOUR": 0,
			"FIVE": 0,
			"SIX": 0,
			"SEVEN": 0,
			"EIGHT": 0,
			"NINE": 0
		}
		b = True
		s = S
	
		a = nums.keys()
		random.shuffle(a)
		for k in a:
			b = True
			#print k
			while b:
				#print (b, s)
				(b, s) = containremove(s, k)	
				if b:
					nums[k] += 1

		if s == "":
			break


	#print nums
	s = '0'* nums["ZERO"]
	s += '1'* nums["ONE"]
	s += '2'* nums["TWO"]
	s += '3'* nums["THREE"]
	s += '4'* nums["FOUR"]
	s += '5'* nums["FIVE"]
	s += '6'* nums["SIX"]
	s += '7'* nums["SEVEN"]
	s += '8'* nums["EIGHT"]
	s += '9'* nums["NINE"]
	return s


def main(argv):

	fout_name = argv[1].split(".")[0] + ".out"
	fout = open(fout_name, "w")

	fin = open(argv[1])
	nb_cases = int(fin.readline())


	for case_no in range(1, nb_cases+1):
		
#		print "Case:", case_no
		S = fin.readline().strip()
		# Have read all stuff for this case:
		fout.write( "Case #{}: {}\n".format(case_no, solve_case(S)))

	fout.close()
	fin.close()
	

import sys
if __name__ == "__main__":
    main(sys.argv)
