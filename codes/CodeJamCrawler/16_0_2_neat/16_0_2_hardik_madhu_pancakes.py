

def flipStack(pancakes, flipLen):
	flippedStack = []

	for i in range(flipLen):
		if pancakes[i] == 0:
			flippedStack.append(1)
		else:
			flippedStack.append(0)

	pancakes[0:flipLen] = flippedStack[::-1]

	return pancakes



T = raw_input()
T = int(T)


for i in range(T):
	pancakeList = []
	smileSide = 0
	blankSide = 0
	lastBlank = 0
	flipped = 0

	s = raw_input()
	for j in range(len(s)):
		if s[j] == '+':
			pancakeList.append(1)
			smileSide += 1
		else:
			pancakeList.append(0)
			blankSide += 1
			lastBlank = j

	if len(pancakeList) == 1:
		if pancakeList[0] == 1:
			writeStr = "Case #"+str(i+1)+": "+str(flipped)
		else:
			flipped += 1
			writeStr = "Case #"+str(i+1)+": "+str(flipped)

		print writeStr
		continue


	#if blankSide > smileSide:
	#	pancakeList = flipStack(pancakeList, lastBlank+1)
	#	flipped += 1
	

	allSmile = 0

	while True:
		if allSmile == 1:
			writeStr = "Case #"+str(i+1)+": "+str(flipped)
			print writeStr
			break

		tempList = []
		if pancakeList[0] == 0:
			blank = 1
			smile = 0
		else:
			blank = 0
			smile = 1

		for j in range(len(pancakeList)):
			if pancakeList[j] == 1:
				if blank == 1 and smile == 0 and len(tempList) != 0:
					pancakeList[0:len(tempList)] = [1]*len(tempList)
					tempList = []
					blank = 0
					flipped += 1
					break
				else:
					if j == len(pancakeList)-1:
						allSmile = 1
						break

					tempList.append(1)
					smile = 1

			if pancakeList[j] == 0:
				if smile == 1 and blank == 0 and len(tempList)!=0:
					pancakeList[0:len(tempList)] = [0]*len(tempList)
					tempList = []
					smile = 0
					flipped += 1
					break
				else:
					if j == len(pancakeList)-1:
						flipped += 1
						allSmile = 1
						break

					tempList.append(0)
					blank = 1
