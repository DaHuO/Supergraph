# -*- coding: utf-8 -*-
import sys
import re
import math
import random

def getNum(index):
	index = index -1
	i = 1
	while index >= pow(10,i-1) * 9 * i:
		index = index - pow(10,i-1) * 9 * i
		i = i + 1
	num = pow(10,i-1) + index // i
	dig = index % i
	return  num // pow(10,i - dig - 1) % 10

def isPrime(n):
	i = 2
	
def addDigit(s,n):
	nn = n
	while nn > 0:
		s.add(nn % 10)
		nn = nn // 10
	
def main():
	LineNumber = None;
	Case = 0
	for line in sys.stdin:
		if LineNumber is None:
			LineNumber = int(line)
		else:
			Case = Case + 1
			if LineNumber == 0:
				break
			LineNumber = LineNumber - 1
			base = int(line)
			if base == 0:
				print("Case #{0}: INSOMNIA".format(Case))
				continue
			curr = 0
			digits = set()
			while (len(digits) < 10):
				curr = curr + base
				addDigit(digits,curr)
			print("Case #{0}: {1}".format(Case,curr))
			
	
if __name__ == '__main__':
	main()