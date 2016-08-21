import sys

numCases = int(input())

for case in range(numCases):
	numParties = int(input())
	inParty = input()
	partyList = inParty.split()
	partyDict = {}
	currentParty = 'A'
	numLeft = 0
	for party in range(numParties):
		numParty = partyList[party]
		numLeft += int(numParty)
		numPartyI = int(numParty)
		if numPartyI in partyDict:
			partyDict[numPartyI] += currentParty
		else:
			partyDict[numPartyI] = currentParty
		currentParty = chr(ord(currentParty) + 1)
	sortedKeys = sorted(partyDict.keys(), reverse = True)

	outputString = ""


	evacCount = 0
	while numLeft > 2:
		key = sortedKeys[0]
		currentList = list(partyDict[key])
		for char in currentList:
			outputString += char
			evacCount += 1
			if evacCount == 2:
				outputString += " "
				evacCount = 0
			numLeft -= 1
			partyDict[key] =  partyDict[key][1:]
			if key-1 in partyDict:
				partyDict[key-1] += char
			else:
				partyDict[key-1] = char
			if numLeft <= 2:
				break
		if numLeft > 2:
			del partyDict[key]
		sortedKeys = sorted(partyDict.keys(), reverse = True)

	if not outputString.endswith(' ') and len(outputString) > 0:
		outputString += " "
	outputString += partyDict[1]

	print("Case #" + str(case+1) + ": " + outputString)	