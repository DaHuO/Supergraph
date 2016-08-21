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

def NerasTactics(stack):
	breaks = 0;
	current = stack[0]
	for c in stack:
		if c != current:
			breaks += 1
			current = c
	if stack[0] == "+":
		if breaks % 2 == 0:
			return breaks
	if stack[0] == "-":
		if breaks % 2 == 1:
			return breaks
	return breaks + 1


for i in range(0, len(cases)):
	outputFile.write("Case #%d: %d\n" % (i+1, NerasTactics(cases[i])))

outputFile.close()