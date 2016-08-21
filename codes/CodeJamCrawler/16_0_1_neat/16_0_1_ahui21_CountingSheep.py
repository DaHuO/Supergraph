import sys

inputFileName = ""
lines = []
outputFileName = ""

def parse_args():
	global inputFileName

	if len(sys.argv) == 2:
		inputFileName = sys.argv[1]
	else:
		raise ValueError('Incorrect number of arguments (%i) found.' % len(sys.argv))

def parse_file():
	global inputFileName
	global lines

	file = open(inputFileName)

	first = True
	numOfLines = 0

	for line in file:
		if first:
			numOfLines = int(line)
			first = False
		else:
			lines.append(line.strip())

	if len(lines) != numOfLines:
		raise ValueError('Incorrect number of lines (%i) found, when expected %i' % (len(lines), numOfLines))

def writeToFile():
	global outputFileName

	if inputFileName[len(inputFileName) - 3:] == '.in':
		outputFileName = inputFileName[0:len(inputFileName) - 3] + '.out'
	else:
		outputFileName = inputFileName + '.out'

	outputFile = open(outputFileName, 'w')

	for i in range(len(lines)):
		number = lines[i]
		try:
			outputFile.write('Case #%i: %s' % (i + 1, checkIndividual(int(number))))
			outputFile.write('\n')
		except:
			raise ValueError('The line %s is not an int' % i)

	outputFile.close()

def checkIndividual(number):
	numOfTrials = 0

	digits = {'0': False, '1': False, '2': False, '3': False, '4': False,
			  '5': False, '6': False, '7': False, '8': False, '9': False,
			  'total': 0}

	if number == 0:
		return 'INSOMNIA'

	while digits['total'] < 10:
		numOfTrials = numOfTrials + 1

		numberToString = str(number * numOfTrials)

		for ch in numberToString:

			if digits[ch] == False:
				digits[ch] = True
				digits['total'] = digits['total'] + 1

	return number * numOfTrials

def main():
	parse_args()
	parse_file()
	writeToFile()

if __name__ == '__main__':
	main()

