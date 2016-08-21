import os
import math

def getDecimalValueOfStringFromBase(jamcoin, base):
	total = 0
	jamcoin = str(jamcoin)
	for i in xrange(0, len(jamcoin)):
		value = int(jamcoin[i])
		multiplier = base**(len(jamcoin)-i-1)
		together = value * multiplier
		total+= value * multiplier
	return total

def hasDivisor(jamcoin, base):
	decimalValue = getDecimalValueOfStringFromBase(str(jamcoin), base)
	for i in xrange(2, int(math.sqrt(decimalValue))+1):
		if decimalValue % i == 0:
			return True
	return False

def getAllPossibleJamcoins(lengthJamcoin):
	allPossibleJamcoins = []
	numMiddleDigits = int(lengthJamcoin)-2
	middleJamcoinValueMax = 2**(numMiddleDigits)
	for jamcoinDecimal in xrange(0, middleJamcoinValueMax):
		jamcoinBinary = '{0:b}'.format(jamcoinDecimal).zfill(numMiddleDigits)
		allPossibleJamcoins.append('1'+str(jamcoinBinary)+'1')
	return allPossibleJamcoins

def getNextPossibleJamcoin(previousPossibleJamcoin):
	middlePreviousPossibleJamcoinBinary = str(previousPossibleJamcoin)[1:-1]
	numMiddleDigits = len(middlePreviousPossibleJamcoinBinary)
	middlePreviousPossibleJamcoinDecimal = int(middlePreviousPossibleJamcoinBinary,2)
	middleNextPossibleJamcoinDecimal = middlePreviousPossibleJamcoinDecimal + 1

	return '1' + '{0:b}'.format(middleNextPossibleJamcoinDecimal).zfill(numMiddleDigits) + '1'

def isValidJamcoin(possibleJamcoin):
	for i in xrange(2, 11):
		if not hasDivisor(str(possibleJamcoin), i):
			return False
	return True
def getJamcoins(lengthJamcoin, numJamcoins):
	jamcoins = []
	zeroes = ''.zfill(int(lengthJamcoin)-2)
	possibleJamcoin = '1' + zeroes + '1'
	while len(jamcoins) != numJamcoins:
		if isValidJamcoin(possibleJamcoin):
			jamcoins.append(possibleJamcoin)
		possibleJamcoin = getNextPossibleJamcoin(possibleJamcoin)
	return jamcoins


def getDivisors(jamcoin):
	divisors = []
	for base in xrange(2, 11):
		value = getDecimalValueOfStringFromBase(jamcoin, base)
		for possibleDivisor in xrange(2, value):
			if value % possibleDivisor == 0:
				divisors.append(str(possibleDivisor))
				break;
	return ' '.join(divisors)



def getJamcoinInfo(lengthJamcoin, numJamcoins):
	jamcoinInfo = []
	jamcoins = getJamcoins(lengthJamcoin, numJamcoins)
	for jamcoin in jamcoins:
		jamcoinInfo.append(jamcoin + ' ' + getDivisors(jamcoin) + '\n')

	return jamcoinInfo

def coinJam():
	with open('input.txt') as input_file:
	    testCases = input_file.readlines()
	numTestCases = testCases[0]
	testCases.remove(numTestCases)
	output_filename = 'output.txt'
	if os.path.exists(output_filename):
		os.remove(output_filename)
	for i in range(0, len(testCases)):
		lengthAndNumJamcoins = testCases[i].split(' ')
		lengthJamcoin = lengthAndNumJamcoins[0]
		numJamcoins = lengthAndNumJamcoins[1]
	 	jamcoinInfo = getJamcoinInfo(lengthJamcoin, int(numJamcoins))
		
		
		with open(output_filename, 'a') as output_file:
			output_file.write('Case #' + str(i+1) + ': ' + '\n')
			for jamcoin in jamcoinInfo:
				output_file.write(jamcoin)

def verify_divisors(string):
	jamcoin_and_divisors = string.split(' ')
	jamcoin = jamcoin_and_divisors[0]
	divisors = jamcoin_and_divisors[1:]
	#print "jamcoin: " + jamcoin
	for i in xrange(0, len(divisors)):
		base = i + 2
		decimalAtBase = getDecimalValueOfStringFromBase(jamcoin, base)
		print "base " + str(base) + ": " + str(decimalAtBase) + " % " + divisors[i] + " = " + str(decimalAtBase%int(divisors[i]))
		#remainder =  decimalAtBase%int(divisors[i])
		#if remainder != 0:
		#	print remainder

coinJam()
#with open('output.txt') as input_file:
#	    divisorLines = input_file.readlines()
#divisorLines.pop(0)
#for divisorLine in divisorLines:
#	verify_divisors(divisorLine)
#for i in xrange(2, 11):
#	print getDecimalValueOfStringFromBase(100000000000010111, i)
#print getDivisors(100000000000010111)