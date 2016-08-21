
def getInput():
	file = open('input.txt', 'r')
	lines = [line.strip('\n').split(' ') for line in file]
	lines.pop(0)
	return lines

def solveLine(k, c, s):
	if k == s:
		return range(1, s+1)
	return ['Impossible']

def output(results):
	outputFile = open('output.txt', 'w')
	for i, result in enumerate(results):
		outputFile.write('Case #' + str(i+1) + ':')
		for number in result:
			outputFile.write(' ' + str(number))
		outputFile.write('\n')
	outputFile.close()
	print results

lines = getInput()
print lines
results = []
for line in lines:
	results.append(solveLine(int(line[0]), int(line[1]), int(line[2])))

output(results)