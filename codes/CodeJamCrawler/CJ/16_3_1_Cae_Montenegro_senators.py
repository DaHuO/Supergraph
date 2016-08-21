import numpy as np

letters = np.asarray(map(chr, range(65, 91)))
outputFile = open("Output.txt", "w")

def solve(case, numParties, numberOfSenators):
	outputFile.write("Case #"+str(case)+":")
	global letters, outputFile
	myLetters = letters[:numberOfSenators.size]
	print(myLetters)
	totalSenators = np.sum(numberOfSenators)

	while totalSenators>0:
		outputFile.write(" ")
		evacuate = []
		while(len(evacuate)<2):
			if len(evacuate) == 1 and np.sum(numberOfSenators)==2:
				evacuate.append(None)
				break
			maxPos = np.argmax(numberOfSenators)
			maxVal = numberOfSenators[maxPos]
			numberOfSenators[maxPos] -= 1
			totalSenators -= 1
			if maxVal == 0:
				evacuate.append(None)
			else:
				evacuate.append(myLetters[maxPos])
		for element in evacuate:
			if element is not None:
				outputFile.write(element)

	outputFile.write("\n")


f = open('A-large.in', 'r')
#f = open('test.txt', 'r')
problems = f.read().splitlines()
problemList = []
solutions = []
testCases = int(problems[0])
print(testCases)
for x in range(testCases):
	numParties = int(problems[2*x+1])
	numberOfSenators = problems[2*x+2].split(" ")
	numberOfSenators = np.asarray(map(int, numberOfSenators))
	print("solve-----------------------------------------------------", numberOfSenators)
	solve(x+1, numParties, numberOfSenators)