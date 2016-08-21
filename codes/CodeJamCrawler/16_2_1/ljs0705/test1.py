import os

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
	for line in output:
		outputFile.write(line + '\n')
	outputFile.close()

alphaDict = {
	'A' : 1,
	'B' : 2,
	'C' : 3,
	'D' : 4,
	'E' : 5,
	'F' : 6,
	'G' : 7,
	'H' : 8,
	'I' : 9,
	'J' : 10,
	'K' : 11,
	'L' : 12,
	'M' : 13,
	'N' : 14,
	'O' : 15,
	'P' : 16,
	'Q' : 17,
	'R' : 18,
	'S' : 19,
	'T' : 20,
	'U' : 21,
	'V' : 22,
	'W' : 23,
	'X' : 24,
	'Y' : 25,
	'Z' : 26,
}
myDict = {
	0: 'ZERO',
	1: 'ONE',
	2: 'TWO',
	3: 'THREE',
	4: 'FOUR',
	5: 'FIVE',
	6: 'SIX',
	7: 'SEVEN',
	8: 'EIGHT',
	9: 'NINE',
}
solutionList = []
resultNumbers = []

def found(subList):
	for i in range(0,28):
		if subList[i] != solutionList[i]:
			return False
	return True

def addList(number, subList):
	string = myDict[number]
	for ch in string:
		index = alphaDict[ch]
		subList[index] += 1

def subsList(number, subList):
	string = myDict[number]
	for ch in string:
		index = alphaDict[ch]
		subList[index] -= 1

def isPossible(number, subList):
	string = myDict[number]
	for ch in string:
		index = alphaDict[ch]
		if subList[index] >= solutionList[index]:
			return False
	return True

def search(number, subList):
	global resultNumbers
	if isPossible(number, subList):
		addList(number, subList)
		resultNumbers.append(number)
		if found(subList):
			return True
		else:
			if search(number, subList)==False:
				subsList(number, subList)
				resultNumbers.pop()
				return search(number+1, subList)
			else:
				return True
	else:
		if number==9:
			return False
		return search(number+1, subList)

def solveProblem(input):
	global solutionList
	global resultNumbers
	solutionList = []
	resultNumbers = []
	for i in range(0,28):
		solutionList.append(0)
	for ch in input:
		index = alphaDict[ch]
		solutionList[index] += 1

	subList = []
	for i in range(0,28):
		subList.append(0)

	return search(0, subList)

# result = solveProblem('ETHER')
# print(str(result))
# print(str(resultNumbers))

lines = readLines('input.txt')
total = int(lines[0])
output = []
for i in range(1, total+1):
	solveProblem(lines[i])
	value = ''
	for number in resultNumbers:
		value += str(number)
	line = 'Case #{0}: {1}'.format(i, value)
	output.append(line)
writeLines(output)