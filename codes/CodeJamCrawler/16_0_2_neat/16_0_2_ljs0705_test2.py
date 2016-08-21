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
	for line in output:
		outputFile.write(line + '\n')
	outputFile.close()

def getFirstDiffPosition(input):
	first = input[0]
	i = 0
	for char in input:
		if char != first:
			return i
		i += 1
	return i

def getReversed(input, pos):
	newChar = ''
	if input[0]=='-':
		newChar = '+'
	else:
		newChar = '-'
	stringFormat = '{:' + newChar + '^' + str(pos) + '}'
	result = '{0}{1}'.format(stringFormat.format(''), input[pos:])
	return result

def isCompleted(input):
	return input.find('-') == -1

def solveProblem(input):
	count = 0
	while True:
		if isCompleted(input):
			return count
		pos = getFirstDiffPosition(input)
		input = getReversed(input, pos)
		count += 1

# def randomInput(size):
# 	input = ''
# 	for i in range(0,size):
# 		if random.randrange(1,10) % 2 == 0:
# 			input += '-'
# 		else:
# 			input += '+'
# 	return input

# input = randomInput(100)
# count = solveProblem(input)
# print('{0} {1}'.format(input, count))

lines = readLines('input.txt')
total = int(lines[0])
output = []
for i in range(1, total+1):
	value = solveProblem(lines[i])
	line = 'Case #{0}: {1}'.format(i, value)
	output.append(line)
	# print(line)
writeLines(output)