#!/usr/bin/python

import sys
import math

def findDivisor(num):
	"an implementation of strassen's algo"
	numSqrt = int(math.sqrt(num))
	divisors = [0] * (numSqrt + 1)
		
	for i in range(2, numSqrt + 1):
		if divisors[i] == 0:
			if num % i == 0:
				return i
			divisors[i] = 1
			for j in range(i * i, numSqrt, i):
				divisors[j] = 1

	return None

def isCoinJam(numStr):
	divisors = []
	for base in range(2, 11):
		divisor = findDivisor(int(numStr, base))
		if divisor is None:
			return None
		divisors.append(divisor)

	return divisors

def findCoinJams(N, J):
	for i in range(0, int(pow(2, N -2)) + 1):
		if J == 0:
			break

		binStr = '1' + bin(i)[2:].zfill(N -2) + '1'
		divisors = isCoinJam(binStr)
		if divisors is None:
			continue

		print '{0} {1}'.format(binStr, ' '.join([str(d) for d in divisors]))
		J -= 1

lineNum = 0
for line in sys.stdin:
	lineNum += 1
	if lineNum == 1:
		continue
	N, J = [int(a) for a in line.split(' ')]
	print 'Case #{0}'.format(lineNum - 1)
	findCoinJams(N, J)
