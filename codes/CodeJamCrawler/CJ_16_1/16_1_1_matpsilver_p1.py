


def getInput():
	file = open('input.txt', 'r')
	cases = [line.strip('\n') for line in file]
	cases.pop(0)
	return cases


def printOutput(output):
	outputFile = open('output.txt', 'w')
	for i, line in enumerate(output):
		outputFile.write('Case #' + str(i+1) + ': ' + line + '\n')
	outputFile.close()


cases = getInput()
print cases

results = []
for case in cases:
	characters = list(case)
	result = ''
	for char in characters:
		r1 = result + char
		r2 = char + result
		result = max(r1, r2)
	results.append(result)

print results
printOutput(results)
