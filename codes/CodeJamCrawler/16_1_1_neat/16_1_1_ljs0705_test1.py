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

def solveProblem(input):
	output = ''
	head = 0
	count = 0
	for ch in input:
		if count==0:
			output = ch
			head = alphaDict[ch]
		else:
			if head <= alphaDict[ch]:
				output = ch + output
				head = alphaDict[ch]
			else:
				output = output + ch
		count += 1
	return output


lines = readLines('input.txt')
total = int(lines[0])
output = []
for i in range(1, total+1):
	value = solveProblem(lines[i])
	line = 'Case #{0}: {1}'.format(i, value)
	output.append(line)
	# print(line)
writeLines(output)