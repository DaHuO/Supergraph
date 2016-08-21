import string

#The logic to give output for each case.
def getTopOne(partyCountList, totalParties):
	top = 0
	for i in range (int(totalParties)):
		if int(partyCountList[top]) <= int(partyCountList[i]):
			top = i
	
	partyCountList[top] = int(partyCountList[top]) - 1

	return 	string.ascii_uppercase[top]

	
#actual logic to read data and print it by calling getOutputString function
outputList = []
runningSum = 0

#string.ascii_uppercase[5] F

with open ('C:/Users/rpant/Desktop/Python_Programs/Round1c/Problem1/input.txt') as data :
	totalNumberOfCases = data.readline().strip()
	for index in range (int(totalNumberOfCases)):
		noOfParties = data.readline().strip()
		partyString = data.readline().strip()
		partCount = partyString.split(" ")		
		
		outString = ''
		
		for i in range (int(noOfParties)):
			runningSum = runningSum + int(partCount[i])
			
		while runningSum > 0:
			#Call the Logic
			if (runningSum % 2 == 0):
				str1 = getTopOne(partCount, noOfParties)
				str1 = str1 + getTopOne(partCount, noOfParties)
				outString = outString + " " + str1
				runningSum = runningSum -2
				
			else:	
				outString = outString + " " + getTopOne(partCount, noOfParties)
				runningSum = runningSum -1
			
		#Append the output
		outputList.append(outString)

with open ('C:/Users/rpant/Desktop/Python_Programs/Round1c/Problem1/output.txt', "w") as os :	
	for index in range(len(outputList)):	
		print('Case #' + str(index+1) + ': ' + str(outputList[index]), file=os)