#!/usr/bin/python
import sys
import math

def main( argv ):
	infile = open(argv[1], 'r')
	outfile = open('D-output.txt', 'w')
	cases = int(infile.readline())
	for case in range(1, cases+1):
		int_list = [int(i) for i in infile.readline().split(" ")]
		sequence = int_list[0]
		complexity = int_list[1]
		gradStudents = int_list[2]
		tiles = getTiles(sequence, complexity, gradStudents)
		print("Case #" + str(case) + ": " + tiles, file=outfile)


def getTiles(sequence, complexity, gradStudents):
	output = []
	if (gradStudents < sequence):
		return 'IMPOSSIBLE'
	totalLen = sequence ** complexity
	segmentLen = int(totalLen/sequence)
	for i in range(sequence):
		position = (segmentLen * i) + 1
		output.append(str(position))
	return ' '.join(output)

def getComplexTiles(length, complexity):
	outfile = open('complextilefile', 'w')
	with open('tilefile', r) as fp:
		for line in fp:
			line = line.rstrip()
			for i in range(len(line)):
				if line[i] == 'L':
					outfile.write(line)
				else:
					outfile.write('G' * length)
				outfile.write('\n')


def getOriginalTiles(length):
	filename = 'tilefile'
	coinList = []
	coin = '1'
	coinList.append(coin)
	tilefile = open(filename + '0', 'w')
	print('L', file=tilefile)
	print('G', file=tilefile)
	tilefile.close()
	for i in range(length):
		infilename = filename + str(i)
		outfilename = filename + str(i+1)
		if i == length-1:
			outfilename = 'tilefile'
		outfile = open(outfilename, 'w')
		with open(infilename, 'r') as fp:
			for line in fp:
				line = line.rstrip()
				outfile.write(line + 'L' + "\n")
				outfile.write(line + 'G' + "\n")
		outfile.close()

if __name__ == "__main__":
    main(sys.argv)