def allInList(numberList):
	for i in range(0, 10):
		if i not in numberList:
			return False
	return True

def helpSleep(number):
	if number == 0:
		return None

	numbers = []
	i = 1
	n = 0
	while True:
		if allInList(numbers):
			break
		n = i * number
		spell = str(n)
		for ch in spell:
			if int(ch) not in numbers:
				numbers.append(int(ch))

		i += 1

	return n

inputFile = open('input.txt')
outputFile = open('output.txt', 'w')
tests = int(inputFile.readline())

for i in range(tests):
	number = int(inputFile.readline().strip())
	if helpSleep(number) == None:
		outputFile.write("Case #" + str(i+1) + ": INSOMNIA\n") 

	else:
		outputFile.write("Case #" + str(i+1) + ": " + str(helpSleep(number)) + "\n")

inputFile.close()
outputFile.close()