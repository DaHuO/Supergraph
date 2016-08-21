import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
inputFile = open(args.filename, 'r')
outputFile = open('output.txt', 'w')

numberOfCases = int(inputFile.readline().strip())

for case in xrange(0,numberOfCases):
	word = inputFile.readline().strip()
	lastWord = ''
	firstLetter = True

	for letter in word:
		if firstLetter:
			lastWord += letter
			firstLetter = False
		else:
			if ord(letter) >= ord(lastWord[0]):
				lastWord = letter + lastWord
			else:
				lastWord = lastWord + letter

	outputFile.write('Case #%d: %s\r\n' % (case+1, lastWord))