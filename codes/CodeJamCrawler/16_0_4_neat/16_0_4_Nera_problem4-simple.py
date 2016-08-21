import sys

if len(sys.argv) != 3:
	print "Usage: problem2 <input file> <output file>"
	exit();

cases = []
inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()
for i in range(1, len(lines)):
	cases += [lines[i].strip()]

outputFile = open(sys.argv[2], "w")

for i in range(0, len(cases)):
	K = int(cases[i].split()[0])
	s = "Case #%d: " % (i + 1)
	for j in range(0, K):
		s += "%d " % (j + 1)
	s += "\n"
	outputFile.write(s)
outputFile.close()