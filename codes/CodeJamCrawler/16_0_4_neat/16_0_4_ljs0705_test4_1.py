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

def solveProblem(k, c, s):
	result = ''
	for i in range(1, k+1):
		result += '{0} '.format(i)
	return result

lines = readLines('input.txt')
total = int(lines[0])
output = []
for i in range(1, total+1):
	inputs = lines[i].split(' ')
	value = solveProblem(int(inputs[0]), int(inputs[1]), int(inputs[2]))
	line = 'Case #{0}: {1}'.format(i, value)
	output.append(line)
	# print(line)
writeLines(output)