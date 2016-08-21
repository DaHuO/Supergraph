#!/usr/bin/python
import sys
happy = '+'
sad = '-'

def main( argv ):
	infile = open(argv[1], 'r');
	outfile = open('output.txt', 'w');
	progress = open('progress.txt', 'w');
	cases = int(infile.readline())
	for case in range(1, cases+1):
		print("Case #" + str(case) + ": ", file=progress)
		lastNum = getMinTimes(infile.readline(), progress)
		print("Case #" + str(case) + ": " + str(lastNum), file=outfile)


def getMinTimes( pancakeString, progress ): 
	happy = '+'
	sad = '-'
	pancakes = list(pancakeString)
	pancakes.remove('\n')
	flips = 0
	tries = 0
	if sad not in pancakes:
		return flips
	while (sad in pancakes):
		print (pancakes, file=progress)
		flip(bottomUnhappyPancake(pancakes), pancakes)
		flips += 1
		tries += 1
	print (pancakes, file=progress)
	if sad not in pancakes:
		return flips
	else :
		return "ERROR"


def flip(num, pancakes):
	for i in range(0, num+1):
		pancakeType = happy if pancakes[i] == sad else sad
		pancakes[i] = pancakeType

def topUnhappyPancake(pancakes):
	for i in range(len(pancakes)):
		if pancakes[i] == sad:
			return i
	return -1

def bottomUnhappyPancake(pancakes):
	for i in range(len(pancakes)-1, -1, -1):
		if (pancakes[i]) == sad:
			return i
	return -1


if __name__ == "__main__":
    main(sys.argv)