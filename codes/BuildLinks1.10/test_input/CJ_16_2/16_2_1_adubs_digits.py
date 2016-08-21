import sys

numCases = int(input())

for case in range(numCases):
	inString = input()
	inList = list(inString)
	inDict = {}
	for char in inList:
		if char in inDict:
			inDict[char] += 1
		else:
			inDict[char] = 1
	outDict = {}
	if 'Z' in inDict:
		numZeros = inDict['Z']
		outDict['0'] = numZeros
		inDict['E'] -= numZeros
		inDict['R'] -= numZeros
		inDict['O'] -= numZeros
	if 'X' in inDict:
		numSixes = inDict['X']
		outDict['6'] = numSixes
		inDict['S'] -= numSixes
		inDict['I'] -= numSixes
	if 'U' in inDict:
		numFours = inDict['U']
		outDict['4'] = numFours
		inDict['F'] -= numFours
		inDict['O'] -= numFours
		inDict['R'] -= numFours
	if 'G' in inDict:
		numEights = inDict['G']
		outDict['8'] = numEights
		inDict['E'] -= numEights
		inDict['I'] -= numEights
		inDict['H'] -= numEights
		inDict['T'] -= numEights
	if 'W' in inDict:
		numTwos = inDict['W']
		outDict['2'] = numTwos
		inDict['T'] -= numTwos
		inDict['O'] -= numTwos
	if 'O' in inDict:
		if inDict['O'] > 0:
			outDict['1'] = inDict['O']
	if 'H' in inDict:
		if inDict['H'] > 0:
			outDict['3'] = inDict['H']
	if 'F' in inDict:
		if inDict['F'] > 0:
			outDict['5'] = inDict['F']
			inDict['I'] -= inDict['F']
	if 'S' in inDict:
		if inDict['S'] > 0:
			outDict['7'] = inDict['S']
	if 'I' in inDict:
		if inDict['I'] > 0:
			outDict['9'] = inDict['I']


	outString = ""
	for i in range(10):
		iChar = str(i)
		if iChar in outDict:
			numChar = outDict[iChar]
			for j in range(numChar):
				outString += iChar

	print("Case #" + str(case+1) + ": " + outString)	