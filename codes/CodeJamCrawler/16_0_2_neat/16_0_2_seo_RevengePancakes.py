#Take top pancake and get the most consecutive same pancake
#swap all of them.
#repeat
HAPPY_SIDE = '+'
BLANK_SIDE = '-'

def swapPancake(pancake):
	if pancake == HAPPY_SIDE:
		return BLANK_SIDE
	elif pancake == BLANK_SIDE:
		return HAPPY_SIDE
	else:
		raise Exception('Should not reach here')

def swapPancakeStack(pancakeList, swapIndex = 0):
	if len(pancakeList) == 1 or swapIndex == 0:
		pancakeList[0] = swapPancake(pancakeList[0])
		return pancakeList

	elif len(pancakeList) == swapIndex:
		for itr, pancake in enumerate(pancakeList):
			pancakeList[itr] = swapPancake(pancakeList[itr])
		return pancakeList

	else:
		swappedPancakes = pancakeList[:swapIndex]
		swappedPancakes.reverse()
		unswappedPancakes = pancakeList[swapIndex:]
		for itr, pancake in enumerate(swappedPancakes):
			swappedPancakes[itr] = swapPancake(pancake)
		swappedPancakes.extend(unswappedPancakes)
		return swappedPancakes

def checkAllSidesAreSame(pancakeList, pancakeSide):
	assert pancakeSide in [HAPPY_SIDE,BLANK_SIDE]
	for pancake in pancakeList:
		if pancake != pancakeSide:
			return False
	return True

with open("B-large.in", 'r') as input:
	numOfTests = int(input.readline().strip())
	for testCase in xrange(numOfTests):
		numOfFlips = 0
		pancakeStack = []
		for pancake in input.readline().strip():
			pancakeStack.append(pancake)

		while not checkAllSidesAreSame(pancakeStack, HAPPY_SIDE):
			if len(pancakeStack) == 1 and pancakeStack[0] != HAPPY_SIDE:
				pancakeStack = swapPancakeStack(pancakeStack)
			elif checkAllSidesAreSame(pancakeStack, BLANK_SIDE):
				pancakeStack = swapPancakeStack(pancakeStack, len(pancakeStack))
			else:
				for itr, pancake in enumerate(pancakeStack):
					if itr == 0:
						topPancake = pancakeStack[itr]
						continue
					if pancake != topPancake:
						pancakeStack = swapPancakeStack(pancakeStack,itr)			
						break
			numOfFlips += 1
		print 'Case #%i: %i' % (testCase + 1,numOfFlips)

