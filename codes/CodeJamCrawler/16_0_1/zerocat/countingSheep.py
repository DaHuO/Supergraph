#!/usr/bin/python
# coding=utf-8
import sys

def getDigits(n):
	digits = []
	if n == 0:
		digits.append(0)
		return digits
	while n :
		temp  = n%10
		digits.append(temp)
		n  /=10
	return digits

def countSheep(n):
	count =1
	mask = [False] * 10
	loop_check = []
	curN = n
	while False in mask:
		curN = count *n
		# check it is in a infinity loop
		if curN in loop_check:
			return "INSOMNIA"

		loop_check.append(curN)
		temp = getDigits(curN)
		for i in temp:
			mask[i] = True
		count +=1

	return str(curN)

file = open(sys.argv[1], 'r')
writeFile = open(str(sys.argv[2]) , 'w')
T = int(file.readline())
for i in range(T):
	n = int(file.readline())
	out = countSheep(n)
	writeFile.write("Case #%i: %s\n"%(i+1, out))

file.close()
writeFile.close()
