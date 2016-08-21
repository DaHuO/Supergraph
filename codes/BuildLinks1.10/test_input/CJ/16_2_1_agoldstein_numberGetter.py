"""
zero - z
six - x
eight - g
four - u
two - w
seven - s
three - r
five - v
nine - i
one - rest
"""
import string

inputString = string.split(open("numbers.in", "r").read(),"\n")
outputFile = open("numbers.out", "w")
numTests = int(inputString.pop(0))

digitList = []


def removeNumber(number, targetLetter, phoneNumber):
	while targetLetter in phoneNumber:
		digitList.append("ZOWHUVXSGI".index(targetLetter))
		for letter in number:
			i = 0
			while i < len(phoneNumber):
				if letter == phoneNumber[i]:
					if i+1 < len(phoneNumber):
						phoneNumber = phoneNumber[0:i] + phoneNumber[i+1:] 
					else:
						phoneNumber = phoneNumber[0:i]
					break
				i += 1
	return phoneNumber

for testNum in range(1,numTests+1):
	phoneNumber = inputString.pop(0)

	digitList = []

	phoneNumber = removeNumber("ZERO","Z",phoneNumber)
	phoneNumber = removeNumber("SIX","X",phoneNumber)
	phoneNumber = removeNumber("EIGHT","G",phoneNumber)
	phoneNumber = removeNumber("FOUR","U",phoneNumber)
	phoneNumber = removeNumber("TWO","W",phoneNumber)
	phoneNumber = removeNumber("SEVEN","S",phoneNumber)
	phoneNumber = removeNumber("THREE","H",phoneNumber)
	phoneNumber = removeNumber("FIVE","V",phoneNumber)
	phoneNumber = removeNumber("NINE","I",phoneNumber)
	phoneNumber = removeNumber("ONE","O",phoneNumber)


	digitList.sort()
	digitString = ""
	for digit in digitList:
		digitString += str(digit)
	outputFile.write("case #" + str(testNum) + ": " + digitString + "\n")
