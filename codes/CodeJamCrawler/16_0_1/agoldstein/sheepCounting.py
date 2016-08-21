

import string

inputString = string.split(open("sheep.in", "r").read(),"\n")

outputFile = open("sheep.out", "w")

numTests = int(inputString.pop(0))




for testNum in range(1,numTests+1):

	digitList = []

	startNum = int(inputString.pop(0))

	for i in range(1,1000):

		for digit in str(i*startNum):
			if digit not in digitList:
				digitList.append(digit)
				
		if len(digitList) == 10:
			outputFile.write("case #" + str(testNum) + ": " + str(i * startNum) + "\n")
			break
		elif i == 999:
			outputFile.write("case #" + str(testNum) + ": " + "INSOMNIA" + "\n")




