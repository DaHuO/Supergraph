import gcjbase

def flipPancakes(inFile):
	stack = inFile.readline().rstrip()
	numberOfFlips = 0
	currentSide = stack[0]

	for pancake in range(1, len(stack)):
		if stack[pancake] != currentSide:
			currentSide = stack[pancake]
			numberOfFlips += 1

	if currentSide == "-":
		numberOfFlips += 1

	return str(numberOfFlips)

gcjbase.run(flipPancakes)