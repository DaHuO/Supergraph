import os
import random

def readLines(filename):
	input = open(filename, 'rb')
	lines = []
	for line in input:
		line = line.replace('\n','')
		lines.append(line)	
	input.close()
	return lines

def writeLines(output):
	outputFile = open('output.txt', 'w')
	outputFile.write(output)
	outputFile.close()

def getNontrivialDivisor(n):
	if n==2 or n==3 or n==5 or n==7: return -1
	if n < 2: return -1
	if n%2 == 0: return 2
	if n%3 == 0: return 3
	r = int(n**0.5)
	f = 5
	count = 0
	while f <= r:
		if n%f == 0: return f
		if n%(f+2) == 0: return f+2
		f +=6
		count += 1
		if count > 500000:
			return -1
	return -1

def getBaseNumber(binary, base):
	result = 0
	for i in range(0,32):
		if binary & 0x01 == 1:
			result += pow(base, i)
		binary = binary >> 1
	return result

def getJamDivisors(binary):
	list = []
	for base in range(2, 11):
		value = getBaseNumber(binary, base)
		divisor = getNontrivialDivisor(value)
		if divisor == -1:
			break
		list.append(divisor)
	return list

def solveProblem(binarySize, total):
	binary = 0x01 << (binarySize-1)
	binary += 1
	results = []
	while True:
		divisors = getJamDivisors(binary)
		if len(divisors) == 9:
			result = '{0} '.format(getBaseNumber(binary, 10))
			for divisor in divisors:
				result += '{0} '.format(divisor)
			results.append(result)
			print('len(results) {0}'.format(len(results)))
			if len(results) == total:
				break
		binary += 2

	output = 'Case #1:\n'
	for result in results:
		output += '{0}\n'.format(result)
	return output

output = solveProblem(32, 500)
writeLines(output)