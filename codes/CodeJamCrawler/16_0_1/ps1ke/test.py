def importFileFromGoogle(fileHere):
	finalDict = {}
	newFile = open(fileHere, "r")
	return newFile.readlines()


def exportFileFromGoogle(listOfResults):
	newFile = open("final.out", "w+")
	i = 1
	for result in listOfResults:
		newFile.write("Case #" + str(i) + ": " + str(result) + "\n")
		i += 1

listIn = importFileFromGoogle("in.in")

numberOfCases = listIn[0]

cases = []

for case in range(1, len(listIn)):
	cases.append(listIn[case])

cases = [case.replace("\n", '') for case in cases]
result = []

for case in cases:
	if case == "0":
		result.append("INSOMNIA")
	else:
		currentTest = case
		numberOfTimes = 0
		listOfDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		while len(listOfDigits) != 0:
			for digit in currentTest:
				for newDigit in listOfDigits:
					if digit == newDigit:
						listOfDigits.remove(newDigit)
			numberOfTimes +=1
			newValue = int(case) * numberOfTimes
			currentTest = str(newValue)

		finalNumber = newValue - int(case)
		result.append(finalNumber)

exportFileFromGoogle(result)
[case.replace("\n", '') for case in cases]