#!/usr/local/bin/python3

convertedValues = []
nonTrivialDivisors = []


def convertToBaseValueOf(jamCoin, base, bitStringLength):
	value = 0
	bitmask = 0x00000001

	for i in range(bitStringLength):
		if (jamCoin & bitmask) > 0:
			value += base ** i
		bitmask <<= 1

	return value


def getBitString(jamCoin, bitStringLength):
	string = ''
	bitmask = 0x80000000

	for i in range(bitStringLength):
		if (jamCoin & bitmask) > 0:
			string += '1'
		else:
			string += '0'
		bitmask >>= 1

	return string


def checkForNonTrivialDivisors():
	areNoPrimes = True

	for i in range(9):
		if (convertedValues[i] % 7 == 0) and (convertedValues[i] != 7):
			nonTrivialDivisors.append(7)
		elif (convertedValues[i] % 3 == 0) and (convertedValues[i] != 3):
			nonTrivialDivisors.append(3)
		elif (convertedValues[i] % 5 == 0) and (convertedValues[i] != 5):
			nonTrivialDivisors.append(5)
		else:
			areNoPrimes = False
			break

	return areNoPrimes


outFile = open('/Users/Michael/Desktop/output', 'w')

bitStringLength = 32
numberOfJamCoins = 500
answersFound = 0

jamCoin = 0x80000001

outFile.write('Case #1:\n')

while(1):
	answerFound = False

	for i in range(9):
		convertedValues.append(convertToBaseValueOf(jamCoin, i + 2, bitStringLength))

	if checkForNonTrivialDivisors():
		answerFound = True
		answersFound += 1

	if answerFound:
		outFile.write(getBitString(jamCoin, bitStringLength) + ' ')

		for i in range(9):
			if i == 9:
				outFile.write(str(nonTrivialDivisors[i]))
			else:
				outFile.write(str(nonTrivialDivisors[i]) + ' ')

		outFile.write('\n')

	if answersFound >= numberOfJamCoins:
		break

	jamCoin += 2
	convertedValues.clear()
	nonTrivialDivisors.clear()

outFile.close()