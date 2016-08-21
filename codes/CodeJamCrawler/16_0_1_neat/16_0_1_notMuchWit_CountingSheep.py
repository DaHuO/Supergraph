def foundAllDigits(numsSeen):
	for digit in numsSeen:
		if numsSeen[digit] == False:
			return False
	return True

def getLastNumberHelper(test, currentNum):
	numsSeen = {}
	# Initialize the numbers seen dictionary to have false for all values.
	for i in range(10):
		numsSeen[str(i)] = False

	# Check all multiples up to 100 since it will begin repeating after that.
	for N in range(100):
		nextMult = currentNum * (N + 1)
		for digit in str(nextMult):
			numsSeen[digit] = True

		if foundAllDigits(numsSeen):
			# Sweet dreams Bleatrix.
			return "Case #" + str(test + 1) + ": " + str(nextMult)

	# Couldn't find all the digits, guess it's no sleep for you Bleatrix.
	return "Case #" + str(test + 1) + ": INSOMNIA"

def getLastNumber():
	with open("A-large.in.txt") as f:
		numberOfTests = int(f.readline())
		for test in range(numberOfTests):
			currentNum = int(f.readline())
			print(getLastNumberHelper(test, currentNum))

getLastNumber()