import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
inputFile = open(args.filename, 'r')
outputFile = open('output.txt', 'w')

numberOfCases = int(inputFile.readline().strip())

for case in xrange(0,numberOfCases):
	pancakes = list(inputFile.readline().strip())
	solved = False
	count = 0

	while not solved:
		if '-' in pancakes:
			count += 1
			lastBlank = ''.join(pancakes).rfind('-')
			for x in xrange(0,lastBlank+1):
				if pancakes[x] == '+':
					pancakes[x] = '-'
				else:
					pancakes[x] = '+'
		else:
			solved = True
			outputFile.write('Case #%d: %d\r\n' % (case+1, count))
