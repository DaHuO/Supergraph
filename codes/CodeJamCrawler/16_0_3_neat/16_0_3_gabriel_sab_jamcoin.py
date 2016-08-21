import random
import math

subCoinPossibilities = []

output = open('output.txt', 'w')

def isprime(number):
	if number % 2 == 0:
		return 2
	if number % 3 == 0:
		return 3
	i = 5
	while i*i <= number:
		if number % i == 0:
			return i
		if number % (i + 2) == 0:
			return i + 2
		i = i + 6
	return number
	
def precomputeSubCoinPossibilities(subLen):
	print subLen
	for i in range(subLen):
		print i
		if i == 0:
			subCoinPossibilities = ["0", "1"]
		else:
			new = []
			for e in subCoinPossibilities:
				new.append("0" + e)
				new.append("1" + e)
			subCoinPossibilities = new
			
def getNextSubCandidate(subcandidate, subLen):
	i = int(subcandidate, 2) + 1
	s = str(bin(i))
	s = s[2:]
	s = s.zfill(subLen)
	return s

def getJamCoins(subLen, numCount):
	ret = []
	#possibilities = subCoinPossibilities
	numPossib = int(math.pow(2, subLen))
	print numPossib
	subcandidate = "0"*subLen
	i = 0
	while i < numPossib:
		if i > 0:
			subcandidate = getNextSubCandidate(subcandidate, subLen)
		candidate = "1" + subcandidate + "1"
		baseNums = []
		for i in range(2, 11):
			baseRepr = int(candidate, i)
			primeResult = isprime(baseRepr)
			if primeResult == baseRepr:
				break
			else:
				baseNums.append(primeResult)
		if len(baseNums) == 9:
			print candidate, baseNums
			ret.append((candidate, baseNums))
		if len(ret) == numCount:
			return ret
		i += 1
	for i in range(numCount - len(ret)):
		ret.append(("impossible", []))
	return ret

with open('input.txt', 'r') as file:
	numberOfCases = int(file.readline())
	for i in range(numberOfCases):
		output.write("Case #" + str(i + 1) + ":\n")
		params = file.readline().split(" ")
		numLen = int(params[0])
		numCount = int(params[1])
		print numberOfCases, numLen, numCount
		subLen = numLen - 2
		#precomputeSubCoinPossibilities(subLen)
		coins = getJamCoins(subLen, numCount)
		for j in range(len(coins)):
			output.write(coins[j][0] + " ")
			for k in range(len(coins[j][1])):
				output.write(str(coins[j][1][k]))
				if k == len(coins[j][1]) - 1:
					if j < numCount - 1:
						output.write("\n")
				else:
					output.write(" ")