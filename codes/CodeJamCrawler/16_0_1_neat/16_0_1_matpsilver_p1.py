
def calculateT (n):
	print n
	if n == '0':
		return 'INSOMNIA'
	firstNumber = int(n)
	currentNumber = 0
	numbersSeen = set()
	while (len(numbersSeen) < 10):
		currentNumber += firstNumber
		numbersSeen |= set(str(currentNumber))
	return currentNumber

file = open('input.txt', 'r')

lines = [line.strip('\n') for line in file]

print lines

numCases = lines.pop(0)
results = [calculateT(line) for line in lines]
outputFile = open('output.txt', 'w')
for i, result in enumerate(results):
	output = "Case #" + str(i+1) + ": " + str(result) + "\n"
	outputFile.write(output)
outputFile.close()
