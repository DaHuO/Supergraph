import sys
import math

T = 0
caseNum = 1

def prime(num):
	if num % 2 == 0:
		return 2
	elif num % 3 == 0:
		return 3
	elif num % 5 == 0:
		return 5
	elif num % 7 == 0:
		return 7
	elif num % 11 == 0:
		return 11
	elif num % 13 == 0:
		return 13
	return None

for line in sys.stdin:
	if T == 0:
		T = int(line)
	else:
		print "Case #" + str(caseNum) + ":"
		coinLength = int(line.split()[0])
		outLength = int(line.split()[1])
		found = 0
		start = int(math.pow(2,coinLength-1) + 1)
		while found < outLength:
			thisOne = bin(start)[2:]
			start += 2
			if thisOne[-1] == "1" and thisOne[0] == "1":
				outString = thisOne
				for base in range(2,11):
					primeResult = prime(int(thisOne,base))
					if primeResult:
						outString += " " + str(primeResult)
					else:
						break

				if len(outString.split()) == 10:
					print outString
					found += 1