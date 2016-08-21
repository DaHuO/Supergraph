def countingSheep (number):
	if number == 0:
		return 'INSOMNIA'
	else:
		index = 1
		allDigits = False
		digitsSeen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		curNumber = number
		while not allDigits:
			curNumber = index * number
			curNumberString = str(curNumber)
			for i in range(len(curNumberString)):
				curChar = curNumberString[i]
				if digitsSeen[int(curChar)] == 0:
					digitsSeen[int(curChar)] = 1
					if allDigitsSeen(digitsSeen):
						allDigits = True
						break;
			index = index + 1
		return curNumber


def allDigitsSeen (digitsSeen):
	for i in range(len(digitsSeen)):
		if digitsSeen[i] == 0:
			return False

	return True 

fileRead = open ('A-small-attempt0.in','r')
fileWrite = open('Counting_Sheep_Output.txt','w')
numTests = int (fileRead.readline())
for i in range (1,numTests+1):
	curNumber = int (fileRead.readline())
	fileWrite.write('Case #' + str(i) + ": ")
	fileWrite.write(str(countingSheep(curNumber)) + "\n")