bleatrixChosenNum = "0"
caseNumber = 0
allNumbersPresent = 0


with open('input.txt','r') as file:
	for line in file:
		#Initialize Variables
		caseNumber = caseNumber + 1
		i = 1						#Counter for multiplication
		iterativeNumbers = 0 		#The number after multiplication
		allNumbersPresent = 0		#Check if all numbers are present or not
		bleatrixChosenNum = line	#Number Bleatrix though of
		
		#1023 is 0b1111111111
		while(allNumbersPresent != 1023):
			iterativeNumbers = str(int(bleatrixChosenNum) * i)
			i = i + 1
			for num in iterativeNumbers:
				initNumber = 0
				initNumber = 1 << int(num)
				allNumbersPresent = allNumbersPresent | initNumber
			if(i > 1000000):
				break
		if(allNumbersPresent == 1023):
			print("Case #" + str(caseNumber) + ": " + str(iterativeNumbers))
		else:	
			print("Case #" + str(caseNumber) + ": INSOMNIA")

				