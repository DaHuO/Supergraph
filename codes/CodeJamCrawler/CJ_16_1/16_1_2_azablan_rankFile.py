import sys
from collections import Counter

def findMissing(lists):
	freq = Counter()
	for l in lists:
		freq += Counter(l)
	missing = [k for k in freq if (int(freq[k]) % 2 == 1)]
	missing = [int(i) for i in missing]
	missing.sort()
	missing = [str(i) for i in missing]	
	return ' '.join(missing)

with open(sys.argv[2]) as inf:
	lines = inf.readlines()
	nCases = lines[0]
	lines = [l.strip('\n') for l in lines[1:]]

outName = sys.argv[1] + "Output.txt"
ouf = open(outName, 'w')

caseNum = 1
i = 0
while i < len(lines):
	n = int(lines[i])
	nLines = int(2 * n - 1)
	inputLines = lines[i + 1:i + nLines + 1]
	lists = [l.split(' ') for l in inputLines]
	ouf.write("Case" + " #" + str(caseNum) + ": " + str(findMissing(lists)) + "\n")
	i += nLines + 1
	caseNum += 1
