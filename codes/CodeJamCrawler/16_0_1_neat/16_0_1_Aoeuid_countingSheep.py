

def getSolution(n):
	n = int(n)
	if (n == 0):
		return "INSOMNIA"
	digits = set()
	updateSet(n, digits)
	idx = 1
	if (len(digits) is 10):
		return str(idx)
	while 1 is 1:
		idx = idx + 1
		updateSet(n * idx, digits)
		if (len(digits) >= 10):
			return str(n * idx)

def updateSet(n, mySet):
	for char in str(n):
		mySet.add(char)


with open ("input.txt", 'r') as myInput:
	with open ("output.txt", 'w') as myOutput:
		for idx, line in enumerate(myInput):
			if (idx == 0):
				continue;
			sol = getSolution(line)
			
			myOutput.write("Case #" + str(idx) + ": " + sol + "\n")
