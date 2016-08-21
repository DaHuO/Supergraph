inputFile = open("../Downloads/A-large (1).in")
outputFile = open("../Downloads/LastWordOutputLarge.out", "w")
lines = inputFile.readline()
lineNumber = 1
cases = [case.replace('\n','') for case in inputFile.readlines()]
for case in cases:
	print(case)
	winning = case[0]
	for letter in list(case[1::]):
		if letter<winning[0]:
			winning = winning+letter
		else:
			winning = letter+winning
	outputFile.write("Case #"+str(lineNumber)+": "+winning+"\n")
	lineNumber+=1