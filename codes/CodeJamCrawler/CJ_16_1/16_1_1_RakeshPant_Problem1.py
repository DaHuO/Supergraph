#The logic to give output for each case.
def getLastWord(a_string):
	lastWord=''
	for letter in a_string:
		if lastWord == '':
			lastWord = letter
			continue
		
		if lastWord[0]<=letter:
			lastWord = str(letter) + str(lastWord) 
		else:
			lastWord = str(lastWord) + str(letter)
	
	return lastWord	

#actual logic to read data and print it by calling getOutputString function
outputList = []

with open ('C:/Users/rpant/Desktop/Python_Programs/Problem1/input.txt') as data :
	totalNumberOfCases = data.readline()
	for index in range (int(totalNumberOfCases)):
		string = data.readline().strip()
		
		#Call the Logic
		lastWord = getLastWord(string)
		
		#Append the output
		outputList.append(str(lastWord))

with open ('C:/Users/rpant/Desktop/Python_Programs/Problem1/output.txt', "w") as os :	
	for index in range(len(outputList)):	
		print('Case #' + str(index+1) + ': ' + str(outputList[index]), file=os)