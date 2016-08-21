REQUIRED_SET = set("0123456789")

INPUT_FILENAME = "A-large.in.txt"
OUTPUT_FILENAME ="A-large.out.txt"

def readFile(filename):
	with open(filename) as f: 
		return [x.strip('\n') for x in f.readlines()]

def getLastNumber(n, partial = set(), multiplier = 0):
	if n == 0:
		return "INSOMNIA"
	partial = partial | getDigits(n * (multiplier + 1))
	if len(REQUIRED_SET - partial) == 0:
		return n * (multiplier + 1)
	else:
		return getLastNumber(n, partial, multiplier + 1)

def getDigits(n):
	return set(str(n))

def writeLine(output, line):
	with open (output, 'a') as f: 
		f.write(line + "\n")


if __name__ == '__main__':
	content = readFile(INPUT_FILENAME)
	for i in range(1, len(content)):
		writeLine(OUTPUT_FILENAME, "Case #" + str(i) + ": " + str(getLastNumber(int(content[i]))))
