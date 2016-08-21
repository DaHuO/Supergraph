import sys

data = []

with open(sys.argv[1], "r") as f:
    for line in f:
        data.append(int(line))

data = data[1:]
outputFile = sys.argv[1][:-2] + "out"

def seenAll(seen):
	for index in seen:
		if index == 0:
			return False
	return True

def digitsSeen(number, seen):
	while number != 0:
		lastDigit = number % 10
		seen[lastDigit] = 1
		number = number / 10

def sheWillFallAsleep(number):
	if number == 0:
		return "INSOMNIA"

	seen = [0 for i in xrange(10)]
	i = 0
	while not seenAll(seen):
		i += 1
		currNumber = i * number
		digitsSeen(currNumber, seen)

	return i * number

with open(outputFile, "w") as f:
	for i in xrange(len(data)):
		lastNumber = sheWillFallAsleep(data[i])
		f.write("Case #" +  str(i+1) + ": " + str(lastNumber)+"\n")