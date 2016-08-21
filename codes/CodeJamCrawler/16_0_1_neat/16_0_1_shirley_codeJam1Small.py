#!/usr/bin/python3

def hasAllDigits(dict):
	allDigits = 1
	for hasDigit in dict.values():
		if int(hasDigit) == 0:
			allDigits = 0
			return allDigits
	return allDigits


def fillDict(dict, N):
	stringN = str(N)
	for i in range(0, len(stringN)):
		dict[stringN[i]] = 1


file = open('input1.txt', 'r')
caseNumber = file.readline()
caseArray = []
text_file = open("output.txt", "w")
for index in range(0, int(caseNumber)) :
	case = int(file.readline())
	count = index+1
	if case == 0:
		caseArray.append("Case #%d: INSOMNIA" % (count))
		text_file.write("Case #%d\n: INSOMNIA" % (count))
	else:
		currentNumber = case
		digitDict = {}
		for index in range(0, 10):
			digitDict[str(index)] = 0
		fillDict(digitDict, currentNumber)
		while(hasAllDigits(digitDict) == 0):
			currentNumber += case
			fillDict(digitDict, currentNumber)
		caseArray.append("Case #%d: %s" % (count, str(currentNumber)))
		text_file.write("Case #%d: %s\n" % (count, str(currentNumber)))
text_file.close()	
print caseArray
	
