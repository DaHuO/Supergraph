class specialDict(dict):
	def __getitem__(self,key):
		try:
			return dict.__getitem__(self,key)
		except:
			self[key]=0
			return  0


def countCharactersinString(given):
	characters=specialDict()
	for letter in given:
		try:
			characters[letter]+=1
		except KeyError:
			characters[letter]=1
	return characters

def searchForDigits(characters):
	frequency=specialDict()
	for key in xrange(10):
		frequency[key]=0

	key='Z'
	a=characters['Z']
	frequency[0]+=a
	characters['Z']=0
	characters['E']-=a
	characters['R']-=a
	characters['O']-=a
	
	key='W'
	a=characters['W']
	frequency[2]+=a
	characters['W']=0
	characters['T']-=a
	characters['O']-=a
	
	key='G'
	a=characters['G']
	frequency[8]+=a
	characters['G']=0
	characters['E']-=a
	characters['I']-=a
	characters['H']-=a
	characters['T']-=a

	key='H'
	a=characters['H']
	frequency[3]+=a
	characters['H']=0
	characters['T']-=a
	characters['R']-=a
	characters['E']-=2*a
	
	key='X'
	a=characters['X']
	frequency[6]+=a
	characters['X']=0
	characters['I']-=a
	characters['S']-=a
	
	key='R'
	a=characters['R']
	frequency[4]+=a
	characters['R']=0
	characters['F']-=a
	characters['O']-=a
	characters['U']-=a
	
	key='O'
	a=characters['O']
	frequency[1]+=a
	characters['O']=0
	characters['N']-=a
	characters['E']-=a
	
	key='F'
	a=characters['F']
	frequency[5]+=a
	characters['F']=0
	characters['I']-=a
	characters['V']-=a
	characters['E']-=a
	
	key='V'
	a=characters['V']
	frequency[7]+=a
	characters['V']=0
	characters['S']-=a
	characters['E']-=2*a
	characters['N']-=a
	
	key='N'
	a=characters['N']
	frequency[9]+=a/2
	characters['N']=0
	characters['I']-=a/2
	characters['E']-=a/2

	return (frequency,characters)

def sanityCheck(characters):
	for key,value in characters.items():
		if value!=0:
			print 'Error letter {0} has count {1}'.format(key,value)


def main(filename):
	inputList=parseInput(filename)
	outputList=[]
	for inputs in inputList:
		characters=countCharactersinString(inputs)
		(frequency, characters)=searchForDigits(characters)
		sanityCheck(characters)
		tempString=''
		for i in xrange(10):
			for j in xrange(frequency[i]):
				tempString+=str(i)
		outputList.append(tempString)
	printResults(outputList)

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
	f=open('codejamDIGITS', 'w')
	for i in xrange(len(resultsList)):
		out=resultsList[i]
		string="Case #{0}: {1}\n".format(i+1, out)
		f.write(string)
	f.close()