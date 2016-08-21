#ord('A')<ord('B')<...<ord('Z')

def orderString(string):
	answer={0:string[0]}
	minIndex=0
	maxIndex=0
	for letter in string[1::]:
		if ord(letter)<ord(answer[minIndex]):
			maxIndex+=1
			answer[maxIndex]=letter
		else:
			minIndex-=1
			answer[minIndex]=letter
	return (minIndex, maxIndex, answer)


def main(filename):
	inputList=parseInput(filename)
	#should be a list of strings
	outputList=[]
	for inputs in inputList:
		outputList.append(orderString(inputs))
	outputStrings=[]
	for minIndex, maxIndex, dictString in outputList:
		tempList=[]
		while minIndex<=maxIndex:
			tempList.append(dictString[minIndex])
			minIndex+=1
		outputStrings.append(''.join(tempList) )
	printResults(outputStrings)

def parseInput(filename):
	f=open(filename, 'r')
	inputVals=f.read()
	f.close()
	inputList=[]
	string=''
	for i in xrange(len(inputVals)):
		if inputVals[i]=='\n':
			inputList.append(string)
			string=''
			#assume file doesn't start with newline
		else:
			string+=inputVals[i]

	if string !='': #otherwise extra new line at EOF can cause failure.
		inputList.append(string)
	if len(inputList)!=int(inputList[0])+1:
		print "Error! Length mismatch."
	del inputList[0] #number of test cases
	return inputList

def printResults(resultsList):
	f=open('codejamLASTWORD', 'w')
	for i in xrange(len(resultsList)):
		out=resultsList[i]
		string="Case #{0}: {1}\n".format(i+1, out)
		f.write(string)
	f.close()