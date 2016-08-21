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

digitHashDict = {
	'1': 0x01,
	'2': 0x02,
	'3': 0x04,
	'4': 0x08,
	'5': 0x10,
	'6': 0x20,
	'7': 0x40,
	'8': 0x80,
	'9': 0x0100,
	'0': 0x0200,
}

def getDigitHash(number):
	hash = 0
	for char in number:
		hash = hash | digitHashDict[char]
	return hash

def solveProblem(input):
	if input=='0':
		return 'INSOMNIA'
	masterHash = 0x03ff
	i = 1
	number = int(input)
	curHash = 0
	while True:
		curNumber = number * i
		curHash |= getDigitHash(str(curNumber))
		if curHash == masterHash:
			return curNumber
		i += 1

# for i in range(0,1000001):
# 	value = solveProblem(str(i))
# 	print('{0}: {1}'.format(i, value))

lines = readLines('input.txt')
total = int(lines[0])
output = []
for i in range(1, total+1):
	value = solveProblem(lines[i])
	line = 'Case #{0}: {1}'.format(i, value)
	output.append(line)
	# print(line)
writeLines(output)