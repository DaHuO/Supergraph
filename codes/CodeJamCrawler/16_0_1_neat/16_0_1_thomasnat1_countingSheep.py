def getDigits(aNumber):
	aString = str(aNumber)
	result = []
	for aChar in aString:
		result.append(int(aChar))
	return result

def formatOutput(index, output):
	 return "Case #{}: {} \n".format(index, output)

def addToOutput(index, output, outputFile):
	if(index % 1000 == 0):
		print index
	outputFile.write(formatOutput(index, output))

#f = open('sampleInput.txt')
#outputFile = open('sampleOut.txt', 'w')
f = open('A-large.in')
outputFile = open('ALargeOutput.out', 'w')

numProblems = f.readline()
testCaseNum = 1

for line in f:

	startNum = int(line)
	done = False
	currentNum = startNum;
	numsSeen = {0: False, 1: False, 2: False, 3: False, 4: False,5: False,6: False,7: False,8: False,9: False}
	while not done:
		for aDigit in getDigits(currentNum):
			numsSeen[aDigit] = True
		done = True
		for aEntry in numsSeen:
			if(numsSeen[aEntry] == False):
				done = False
		if done:
			addToOutput(testCaseNum, currentNum, outputFile)
		else:
			currentNum = currentNum + startNum
			if currentNum == startNum:
				done = True 
				addToOutput(testCaseNum, "INSOMNIA", outputFile)
	testCaseNum += 1


