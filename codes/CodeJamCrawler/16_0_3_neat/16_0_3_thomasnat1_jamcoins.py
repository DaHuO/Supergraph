def baseChange(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return baseChange(n//base,base) + convertString[n%base]

def formatOutput(index, output):
	 return "Case #{}: {} \n".format(index, output)

def addToOutput(index, output, outputFile):
	if(index % 1000 == 0):
		print index
	outputFile.write(formatOutput(index, output))

def isPrime(aNum):
	for i in range(2, aNum/2):
		if aNum % i == 0:
			return False
	return True

def findFactor(aNum):
	for i in range(2, aNum/2):
		if aNum % i == 0:
			return i

def dictHasKey(aDict, aKey):
	try:
		aDict[aKey] = aDict[aKey]
		return True
	except KeyError:
		return False


f = open('sampleInput.txt')
outputFile = open('sampleOut.txt', 'w')
#f = open('B-large.in')
#outputFile = open('BlargeOutput.out', 'w')

numProblems = f.readline()
testCaseNum = 1

N, J = f.readline().split()
N = int(N)
J = int(J)
numFound = 0




minPossible = 2**(N-1) + 1
maxPossible = (2**N) - 1

coinsFound = 0

for i in range(0, 10000000):
	testNumDecimal = (i*2) + minPossible
	inBinary = baseChange(testNumDecimal, 2)
	#print "analyzing number: ", inBinary
	baseFactors = list()
	for i in reversed(range(2,11)):	
		baseInterp = int(str(inBinary), i)
		for j in range(2, 100):
			if baseInterp % j == 0:
				baseFactors.append(j)
				#print baseInterp, " base: ", i, " has factor ", j
				break
	if len(baseFactors) == 9:
		coinsFound += 1
		print inBinary, 
		for aNum in reversed(baseFactors):
			print aNum, 
		print ""
		if coinsFound == J:
			print "Done"
			break













# factorsOf = dict()

# for i in range(0, 1):
# 	testNumDecimal = (i*2) + minPossible
# 	inBinary = baseChange(testNumDecimal, 2)
	
# #	aFactor = findFactor(testNumDecimal)
	
# 	print testNumDecimal, "(",inBinary,")"
	
# 	#step through the different base interpretations 
# 	for i in range(3,11):	
# 		baseInterp = int(str(inBinary), i)

# 		if dictHasKey(factorsOf, baseInterp):
# 			pass
# 		else:
# 			pass 
# #			factorsOf[baseInterp] = findFactor(baseInterp)
		


# 	# for j in range(2, 10):
# 	# 	if testNum * j < maxPossible:
# 	# 		factorsOf[testNum * j] = aFactor

# 	print factorsOf


# # print "start"
# # #for potentialNumber in range((2**(N-1)) + 1, (2**(N-1)) + 1 + 1):
# # for potentialNumber in range((2**(N-1)) + 1, (2**N) - 1):
# # 	inBinary = baseChange(potentialNumber, 2)
	
# # 	print "starting Bindary: ", inBinary
	
# # 	for i in range(2, 11):
# # 		decimalInterp = int(inBinary, i)
# # 		print "decimal interp: ", decimalInterp

# # 		if isPrime(decimalInterp):
# # 			print "dirty prime"
# # 			break
# # 		if i == 10:
# # 			print "yay jam"













