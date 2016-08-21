import sys
from itertools import *
from sets import Set

def listOfDigits(inputVar):
	return list(map(int, str(inputVar)))


if __name__ == "__main__":
	print 'Input \t Output'

	inputFile = 'input_large.txt'
	with open(inputFile, 'r') as f:
		lines = f.readlines()
		lineCount = 1
		for i in lines:
			seenDigits = set()
			# read input
			inputVar = int(i)
			Ninput = 0
			# small data set
			for i in range(1, 1000000):
				Ninput = i * inputVar;
				for i in listOfDigits(Ninput):
					seenDigits.add(i)

				if len(seenDigits) == 10:
					break

			result = ""
			if len(seenDigits) != 10:
				result = 'INSOMNIA'
			else:
				result = Ninput

			print "Case #"+str(lineCount)+":", result
			lineCount+=1;

