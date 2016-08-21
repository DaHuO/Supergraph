def flip(stack, index):
	flipped=stack[index::-1]
	stack=[1-cake for cake in flipped]+stack[index+1::]

'''recursive variant turns out to be equivalent to greedy algorithm'''
	#doing this process backwards (1 1 1 1 1)->start uses same number of steps
def backwardsFlipSearch(stack,happy,flipCount):
	if len(stack)==0:
		return flipCount

	if stack.pop(-1)==happy:
		flipCount=backwardsFlipSearch(stack,happy,flipCount)
	else:
		flip(stack,-1)
		flipCount+=1
		flipCount=backwardsFlipSearch(stack, 1-happy, flipCount)

	return flipCount


def main(filename):
	f=open(filename, 'r')
	inputVals=f.read()
	f.close()
	inputList=[]
	string=''
	for i in xrange(len(inputVals)):
		if inputVals[i]=='\n':
			inputList.append(string)
			string=''
		else:
			string+=inputVals[i]

	if string !='': #otherwise extra new line at EOF can cause failure.
		inputList.append(string)
	if len(inputList)!=int(inputList[0])+1:
		print "Error! Length mismatch."
	del inputList[0]

	intInputList=[]
	for inp in inputList:
		intInputList.append([(1 if d=='+' else 0) for d in inp])


		resultsList=[]
	for stack in intInputList:
		count=backwardsFlipSearch(stack, 1, 0)
		resultsList.append( count )

	printResults(resultsList)


def printResults(resultsList):
	f=open('codejampancakeOUTPUT', 'w')
	for i in xrange(len(resultsList)):
		out=resultsList[i]
		string="Case #{0}: {1}\n".format(i+1, out)
		f.write(string)
	f.close()
