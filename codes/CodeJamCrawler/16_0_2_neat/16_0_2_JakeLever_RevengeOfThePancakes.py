import fileinput

def generatePossibleStates(state):
	newStates = []

	for flipSize in range(1,len(state)+1):
		toFlip = state[:flipSize]
		notFlip = state[flipSize:]
		flipped = list(reversed( [ not s for s in toFlip ] ))
		newState = flipped + notFlip
		newStates.append(newState)

	return newStates

def solvePancake(origState):
	toProcess = [(0,origState)]
	processed = set()
	while True:
		moveCount,state = toProcess[0]
		toProcess = toProcess[1:]
		processed.add(tuple(state))

		if all(state):
			return moveCount

		newStates = generatePossibleStates(state)
		for newState in newStates:
			if not tuple(newState) in processed:
				toProcess.append((moveCount+1,newState))


caseCount = None
for i,line in enumerate(fileinput.input()):
	line = line.strip()
	if caseCount is None:
		caseCount = int(line)
	else:
		state = [ c=="+" for c in line ]
		print "Case #%d: %s" % (i,solvePancake(state))



#state = [False,False,True,False]
#print solvePancake(state)
#print state
#print "-"*30
#for newState in generatePossibleStates(state):
#	print newState
