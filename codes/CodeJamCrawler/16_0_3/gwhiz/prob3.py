from math import sqrt
numSolutions = 0
def main():
	t = input()
	n, j = raw_input().split()
	n, j = int(n), int(j)
	firstNum = (1 << (n - 1) | 1 << 0)
	print 'Case #1:'
	global numSolutions
	numSolutions = j
	printAns(firstNum, set([]), [i for i in xrange(1, n - 1)])

def isPrime(num):
	num = bin(num)[2:]
	for base in xrange(2, 11):
		newNum = int(num, base)
		i = 2
		prime = True
		while i <= sqrt(newNum):
			if newNum % i == 0: 
				prime = False
				break
			i += 1
		if prime: return True
	return False

def printAns(currentNum, seenNums, zeroPositions):
	global numSolutions
	if numSolutions == 0: return
	for currentPos in xrange(len(zeroPositions)):
		if currentNum not in seenNums:
			seenNums.add(currentNum)
			if not isPrime(currentNum):
				printFactors(currentNum)
				numSolutions -= 1
		# if currentPos == len(zeroPositions):
		# 	return
		from copy import deepcopy
		zeroPositionsCopy = deepcopy(zeroPositions)
		zeroPositionsCopy.remove(zeroPositions[currentPos])
		# print (bin(currentNum | (1 << zeroPositions[currentPos]))[2:], 
		# 		seenNums, zeroPositionsCopy, numSolutions)
		printAns((currentNum | (1 << zeroPositions[currentPos])), 
				seenNums, zeroPositionsCopy)




def printFactors(currentNum):
	num = bin(currentNum)[2:]
	print num,
	for base in xrange(2, 11):
		newNum = int(num, base)
		i = 2
		while i <= newNum/2:
			if newNum % i == 0:
				if base == 10:
					print i
				else:
					print i,
				break
			i += 1



main()