import sys

MAX_ATTEMPTS = 1000

if len(sys.argv) != 3:
	print "Usage: problem1 <input file> <output file>"
	exit();

cases = []
inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()
for i in range(1, len(lines)):
	cases += [int(lines[i])]

outputFile = open(sys.argv[2], "w")

def seenAll(seen):
	ret = True
	for i in seen:
		ret = ret and i
	return ret

for case in range(0, len(cases)):
	N = cases[case]
	if N == 0:
		outputFile.write("Case #%d: INSOMNIA\n" % (case + 1))
		continue

	seen = [False] * 10
	for i in range(1, MAX_ATTEMPTS):
		for c in str(N * i):
			seen[int(c)] = True
		if seenAll(seen):
			outputFile.write("Case #%d: %d\n" % (case + 1, N * i))
			break
		if i == MAX_ATTEMPTS - 1:
			print "Tried out max attempts and no luck! N: %d" % N

outputFile.close()