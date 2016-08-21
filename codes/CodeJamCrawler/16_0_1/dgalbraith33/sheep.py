
def parseInput():
	num = int(raw_input())
	inputs = []
	for i in range(num):
		inputs.append(int(raw_input()))
	return inputs

def getCount(i):
	if i == 0:
		return "INSOMNIA"
	n = i
	found = set()
	while len(found) < 10:
		for c in str(n):
			found.add(int(c))
		n += i
	return str(n - i)

def runTests(inputs):

	for i in range(len(inputs)):
		print "Case #%i: %s" % (i+1, getCount(inputs[i]))


runTests(parseInput())