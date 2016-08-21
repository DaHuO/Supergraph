import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
inputFile = open(args.filename, 'r')
outputFile = open('output.txt', 'w')

numberOfCases = int(inputFile.readline().strip())

for case in xrange(0,numberOfCases):
	n = int(inputFile.readline().strip())
	count = 1
	solved = False
	if n == 0:
		outputFile.write('Case #%d: INSOMNIA\r\n' % (case+1))
		solved = True
	digits = {
		0: 0,
		1: 0,
		2: 0,
		3: 0,
		4: 0,
		5: 0,
		6: 0,
		7: 0,
		8: 0,
		9: 0
	}

	while not solved:
		nDigits = count * n
		for i in str(nDigits):
			digits[int(i)] = 1

		solved = True
		for j in xrange(0,10):
			if digits[j] == 0:
				solved = False

		if solved:
			outputFile.write('Case #%d: %d\r\n' % (case+1, nDigits)) 
		else:
			count += 1