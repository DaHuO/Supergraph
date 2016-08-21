import fileinput
import math
import random
import sys

def getSmallestDivisor(num):
	for i in range(2,int(math.sqrt(num))+2):
		if (num%i) == 0:
			return i
	return None

def isJamcoin(numStr):
	smallestDivisors = []
	for base in range(2,11):
		num = int(numStr,base)
		smallestDivisor = getSmallestDivisor(num)
		smallestDivisors.append(smallestDivisor)
	return smallestDivisors


def generatePossibleJamcoin(l):
	middleBit = [ random.choice(["0","1"]) for i in range(l-2) ]
	return "1" + "".join(middleBit) + "1"
	
random.seed()

caseCount = None
for i,line in enumerate(fileinput.input()):
	line = line.strip()
	if caseCount is None:
		caseCount = int(line)
	else:
		N,J = map(int,line.split())
		print "Case #%d:" % i
		
		used = set()
		while len(used) < J:
				#print isJamcoin("110111")
			possibleJamcoin = generatePossibleJamcoin(N)
			if possibleJamcoin in used:
				continue
			divisors = isJamcoin(possibleJamcoin)
			if None in divisors:
				continue
			print possibleJamcoin + " " + " ".join(map(str,divisors))
			used.add(possibleJamcoin)
			print >> sys.stderr, "%d %s" % (len(used),possibleJamcoin)

