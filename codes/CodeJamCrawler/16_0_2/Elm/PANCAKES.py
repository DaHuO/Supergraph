import sys

def CheckLine(original: str) -> str:
	pancakes = [True if '+' == x else False for x in original]
	currentPancake = pancakes[0]
	flipCount = 0
	for pancake in pancakes[1:]:
		if currentPancake != pancake:
			flipCount += 1
			currentPancake = not currentPancake 
	if not currentPancake:
		flipCount += 1
	return str(flipCount)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		f = open(sys.argv[1], 'r')
		lines = f.readlines()[1:]
		f.close()
	else:
		numberOfCases = int(sys.stdin.readline().strip())
		lines = [None] * numberOfCases
		for i in range(numberOfCases):
			lines[i] = sys.stdin.readline()

	for i, line in enumerate(lines):
		sys.stdout.write("Case #" + str(i+1) + ": " + CheckLine(line.strip()) + "\n")
