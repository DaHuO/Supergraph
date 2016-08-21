def formatOutput(index, output):
	 return "Case #{}: {} \n".format(index, output)

def addToOutput(index, output, outputFile):
	if(index % 1000 == 0):
		print index
	outputFile.write(formatOutput(index, output))

def flipStack(aStack, howMany):
	newStack = aStack[0:howMany]
	for index, pancake in enumerate(newStack):
		if pancake == '+':
			newStack[index] = '-'
		else:
			newStack[index] = '+'
	newStack.reverse()
	return newStack

def indexOfFirstMinus(aStack):
	for index, pancake in enumerate(aStack):
		if pancake == '-':
			return index

def indexOfLastMinus(aStack):
	
	for index, pancake in enumerate(reversed(aStack)):
		if pancake == '-':
			return len(aStack) - index - 1

def isDone(aStack):
	for pancake in aStack:
		if pancake == '-':
			return False
	return True

#f = open('sampleInput.txt')
#outputFile = open('sampleOut.txt', 'w')
f = open('B-large.in')
outputFile = open('BlargeOutput.out', 'w')

numProblems = f.readline()
testCaseNum = 1

for aLine in f:
	aStack = list(aLine[0:-1])

	numFlips = 0
	while not isDone(aStack):
		firstMinus = indexOfFirstMinus(aStack)
		lastMinus = indexOfLastMinus(aStack)

		if firstMinus == 0:
			aStack = flipStack(aStack, lastMinus+1) + aStack[lastMinus+1::]
		else:
			#flip all the front +s 
			aStack = flipStack(aStack, firstMinus) + aStack[firstMinus::]

		numFlips += 1
	
	addToOutput(testCaseNum, numFlips, outputFile)
	testCaseNum += 1







