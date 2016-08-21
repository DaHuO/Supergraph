#!/usr/bin/python
import sys

'''
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a single number N, the number Bleatrix has chosen.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last number that Bleatrix will name before falling asleep, according to the rules described in the statement.

'''


def countSheep(input):
	# num of test cases:
	vals = input.split('\n')
	for i in range(1,len(vals)-1):		
		if int(vals[i]) == 0:
			print "Case #%d: INSOMNIA" % i
			continue

		result = doCounting(int(vals[i]))
		if result == "INSOMNIA":
			print "Case #%d: %s" % (i, result)
		else:
			print "Case #%d: %d" % (i, result)


def doCounting(num):
	'''
	returns last number else insomnia 
	'''
	digits = set()
	for i in range(1,1000000):
		_num = num*i
		for d in str(_num):
			if int(d) not in digits:
				digits.add(int(d))			
			if len(digits) == 10:				
				return _num
	return "INSOMNIA"
	
if __name__ == '__main__':	
	_input = sys.stdin.read()
	countSheep(_input)
#if name == '__main__':
#sample = "6\n0\n1\n2\n11\n1692\n5"
#sample = "1\n1"
#countSheep(sample)