#!/usr/bin/python
import sys

def main( argv ):
	infile = open(argv[1], 'r');
	outfile = open('output.txt', 'w');
	cases = int(infile.readline())
	for case in range(1, cases+1):
		lastNum = getLastNum(int(infile.readline()))
		print("Case #" + str(case) + ": " + str(lastNum), file=outfile);


def getLastNum( originalNum ): 
	if originalNum == 0:
		return "INSOMNIA"
	numArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	tries = 0
	multiplier = 1
	lastNum = originalNum
	while len(numArray) > 0 and tries < 1000:
		lastNum = originalNum * multiplier
		currentArray = list(str(lastNum))
		for num in currentArray:
			if num in numArray:
				numArray.remove(num)
		multiplier += 1
		tries += 1
	if len(numArray) == 0:
		return lastNum
	else:
		return "INSOMNIA"

if __name__ == "__main__":
    main(sys.argv)