#!/usr/bin/env python

ALL_DIGITS = 2**10 - 1

def addDigitsFromNumToMap(n, digitMap):
	while n > 0:
		d = n % 10
		digitMap = digitMap | 2**d
		n /= 10
	return digitMap
		

def isMapComplete(digitMap):
	return digitMap == ALL_DIGITS


def solve(n):
	if n < 1:
		return "INSOMNIA"
		
	digitMap = 0
	currentN = n
	while 1:
		digitMap = addDigitsFromNumToMap(currentN, digitMap)
		if isMapComplete(digitMap):
			return currentN
		currentN += n


def main():
	testCases = int(raw_input())
	for case in xrange(1, testCases + 1):
		n = int(raw_input())
		print 'Case #%d: %s' % (case, str(solve(n)))


if __name__ == '__main__':
	main()
