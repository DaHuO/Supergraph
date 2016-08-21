import sys
from os import linesep as sep
from typing import Tuple

def CheckLine(original: str) -> str:
	if "0" == original:
		return "INSOMNIA"
	numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	i = 1
	line = original
	while True:
		for digit in line:
			try:
				numbers.remove(int(digit))
			except ValueError:
				pass
		if len(numbers) == 0:
			return line
		i += 1
		line = str(i * int(original))
	return str(i)

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
