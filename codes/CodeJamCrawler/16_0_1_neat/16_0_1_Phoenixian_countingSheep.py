def containsDigits(input):
	digits = []
	if input == 0: 
		digits.append(0)
	while input > 0:
		digits.append(input % 10)
		input = input // 10
	return digits
	
def containsAllDigits(input):
	for digit in range(10):
		if digit not in input:
			return False
	return True
def answer(output, number):
	print("Case #" + str(number) + ": " + str(output))

numCases = int(input())
for casenumber in range(1, numCases + 1):
	chosenNumber = int(input())
	currentNumber = chosenNumber
	digitsSeen = containsDigits(chosenNumber)
	if chosenNumber == 0:
		answer("INSOMNIA", casenumber)
	else:
		while not containsAllDigits(digitsSeen):
			currentNumber += chosenNumber
			digitsSeen += containsDigits(currentNumber)
		answer(currentNumber, casenumber)