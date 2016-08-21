def checkdigits(num, boolDig):
	a=str(num)
	for i in xrange(10):
		if str(i) in a:
			boolDig[i]=1

def findLastNumber(sheepNumber):

	if sheepNumber==0:
		return 'INSOMNIA'

	boolDig=[0 for d in xrange(10)]
	ind=1

	while ind<1000:
		checkdigits(sheepNumber*ind, boolDig)
		if sum(boolDig)==10:
			return ind*sheepNumber
		ind+=1

	print 'N=1000, that seems wrong.'

def printResults(resultsList):
	f=open('codejamsheepOUTPUT', 'w')
	for i in xrange(len(resultsList)):
		out=resultsList[i][1]
		string="Case #{0}: {1}\n".format(i+1, out)
		f.write(string)
	f.close()


def main(filename):
	f=open(filename, 'r')
	inputVals=f.read()
	f.close()
	inputList=[]
	string=''
	for i in xrange(len(inputVals)):
		if inputVals[i]=='\n':
			inputList.append(int(string))
			string=''
		else:
			string+=inputVals[i]

	if string !='': #otherwise extra new line at EOF can cause failure.
		inputList.append(int(string))
	if len(inputList)!=inputList[0]+1:
		print "Error! Length mismatch."
	del inputList[0]
	main2(inputList)

def main2(inputList):
	resultsList=[]
	for numbers in inputList:
		outp=findLastNumber(numbers)
		resultsList.append([numbers, outp])
	printResults(resultsList)