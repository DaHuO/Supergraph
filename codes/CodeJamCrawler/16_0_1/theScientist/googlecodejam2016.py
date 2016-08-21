# googlecodejam2016.py

def getTestCases():
	"""
		returns a list of entries.
	"""

	f = open('A-large.in','r')
	inputList = []
	for line in f:
		inputList.append(int(line))

	numEntries = inputList[0]

	inputList = inputList[1:]
	assert(len(inputList)==numEntries)

	return inputList



def formatAndOutput(outputArray):
	"""
		formats the provided array into new line strings
		and outputs it on screen.
	"""
	caseNumber=1
	for output in outputArray:
		print "Case #{0}: {1}".format(caseNumber,output)
		caseNumber+=1

def countingSheep():
	listOfN = getTestCases()

	outputVals = []
	for n in listOfN:
		outputVals.append(solveCountingSheepForN(n))
	formatAndOutput(outputVals)


def solveCountingSheepForN(n,seenNums = set(),mult=1):

	if n==0:
		return 'INSOMNIA'

	def digitsInInt(i):
			return  map(lambda a : int(a),list(str(i)))
	digitsInN = digitsInInt(n*mult)

	#add digits to set.
	seenNums = seenNums.union(set(digitsInN))

	if len(seenNums)>=10:
		return str(n*mult)
	else:
		return solveCountingSheepForN(n,seenNums,mult+1)

countingSheep()


def testDigitsInInt():
	print 'testing digits in int...',
	assert(digitsInInt(10)==[1,0])
	assert(digitsInInt(1523) == [1,5,2,3])
	assert(digitsInInt(01)==[1])
	print  'test complete.'


