

def solveStack (stack):
	current = stack[0]
	count = 0
	for pancake in stack[1:]:
		if current != pancake:
			current = pancake
			count +=1

	if stack[-1] == '-':
		count += 1
	return count






file = open('input.txt', 'r')

lines = [line.strip('\n') for line in file]
print lines
lines.pop(0)

results = [solveStack(line) for line in lines]

outputFile = open('output.txt', 'w')
for i, result in enumerate(results):
	output = "Case #" + str(i+1) + ": " + str(result) + "\n"
	outputFile.write(output)
outputFile.close()
