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
	K = case.split()[0]
	C = case.split()[1]
	S = case.split()[2]

	if float(S) / float(K) <= 0.5:
		result.append("IMPOSSIBLE")
	else:
		listResult = []
		for m in range(0, int(K)):
			listResult.append(str(m+1))
		finalResult = ""
		for number in listResult:
			finalResult = finalResult + number + " "
		result.append(finalResult)

exportFileFromGoogle(result)