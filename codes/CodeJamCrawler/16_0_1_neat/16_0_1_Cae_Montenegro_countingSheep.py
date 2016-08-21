def getDigitsFromNum(myinteger):
	digits = []
	number_string = str(myinteger)
	for ch in number_string:
		digits.append(ch)
	return digits

def resolveProblem(problem):
	digitsKnown = []
	lastNumber = -1
	multiplier = 1
	while len(digitsKnown)<10 and problem*multiplier != lastNumber:
		lastNumber=problem*multiplier
		#print(lastNumber)
		digits = getDigitsFromNum(lastNumber)
		for digit in digits:
			if digit not in digitsKnown:
				digitsKnown.append(digit)
				if len(digitsKnown) >=10:
					return lastNumber
		multiplier += 1
	return "INSOMNIA"

f = open('A-large.in', 'r')
problems = int(f.readline())
print(problems)
problemList = []
for x in range(problems):
	problemList.append(int(f.readline()))

outputFile = open("Output.txt", "w")
count=1
for pro in problemList:
	result = resolveProblem(pro)
	print("result ", result)
	outputFile.write("Case #"+str(count)+": "+str(result)+"\n")
	count+=1
outputFile.close()

