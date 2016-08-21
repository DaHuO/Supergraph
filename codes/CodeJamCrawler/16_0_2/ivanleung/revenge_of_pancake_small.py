import sys
from itertools import *
from sets import Set
from math import pow

def numberOfFlips(inputVar):
	if '-' not in inputVar:
		return 0
	firstIndexOfSad = inputVar.rindex('-')
	#print firstIndexOfSad
	#print inputVar
	#print inputVar[:firstIndexOfSad+1]
	#print flipPancake(inputVar[:firstIndexOfSad+1])
	return 1 + numberOfFlips(flipPancake(inputVar[:firstIndexOfSad+1]))

def flipPancake(inputStr):
	resultStr = ""
	for s in inputStr:
		if s == '+':
			resultStr += '-'
		else:
			resultStr += '+'
	return resultStr

if __name__ == "__main__":
	inputFile = 'input.txt'

	with open(inputFile, 'r') as f:
		lines = f.readlines()
		lineCount = 1
		for i in lines:
			#large data set
			result = numberOfFlips(i)
			print "Case #"+str(lineCount)+":", result
			lineCount+=1;


