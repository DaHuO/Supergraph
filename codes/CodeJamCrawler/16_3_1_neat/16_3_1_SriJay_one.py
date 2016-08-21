def evacuationPlan(senators):
	evacuationPlan=[]
	while True:
		senators.sort(key=lambda x:x[1],reverse=True)
		if senators[0][1]>senators[1][1]:
			evacuationPlan+=senators[0][0]
			evacuationPlan.append(' ')
			senators[0][1]-=1
		elif senators[0][1]>1:
			senators[0][1]-=1
			senators[1][1]-=1
			evacuationPlan.append(senators[0][0])
			evacuationPlan.append(senators[1][0])
			evacuationPlan.append(' ')
		else:
			if sum(zip(*senators)[1]) %2==1:
				evacuationPlan+=senators[0][0]
				evacuationPlan.append(' ')
				del senators[0]			
			while senators:
				evacuationPlan.append(senators[0][0])
				evacuationPlan.append(senators[1][0])
				del senators[0]
				del senators[0]
			return ''.join(evacuationPlan)

def main(filename):
	inputList=specificParse( parse2(parseInput(filename)) )
	outputList=[]
	for case in inputList:
		outputList.append( evacuationPlan(case) )

	printResults(outputList)

def specificParse(inputList):
	j=0
	usableInput=[]
	while j<len(inputList):
		n=int(inputList[j])
		j+=1
		senators=[]
		for i in xrange(n):
			letter=chr(65+i)
			senators.append( [letter, int(inputList[j+i]) ] )
		j+=n
		usableInput.append(senators)
	return usableInput


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
	if len(inputList)!=2*int(inputList[0])+1:
		print "Error! Length mismatch."
	del inputList[0] #number of test cases
	return inputList

def parse2(inputList):
	#parse by whitespace
	processed=[]
	for string in inputList:
		tempString=''
		for char in string:
			if char==' ':
				processed.append(tempString)
				tempString=''
			else:
				tempString+=char
		processed.append(tempString)

	return processed

def printResults(resultsList):
	f=open('codejam', 'w')
	for i in xrange(len(resultsList)):
		out=resultsList[i]
		string="Case #{0}: {1}\n".format(i+1, out)
		f.write(string)
	f.close()