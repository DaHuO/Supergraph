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
	numberOfTurns = 0
	panks = list(case)
	lent = len(panks)
	print panks

	i = 1
	while i <= lent:
		if panks[lent - i] == "+":
			if lent - i == 0:
				result.append(numberOfTurns)
				pass
			i+=1
		else:
			for j in range(0,lent-i + 1):
				if panks[j] == "-":
					panks[j] = "+"
				else:
					panks[j] = "-"
			numberOfTurns += 1

exportFileFromGoogle(result)