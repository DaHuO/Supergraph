from collections import Counter
import sys

digit = [
	Counter('ZERO'),
	Counter('ONE'),
	Counter('TWO'),
	Counter('THREE'),
	Counter('FOUR'),
	Counter('FIVE'),
	Counter('SIX'),
	Counter('SEVEN'),
	Counter('EIGHT'),
	Counter('NINE')
]


def getDigits(scount, n):
	i = n
	num = ""
	while i < len(digit):
		if contains(scount, digit[i]):
			thisScount = scount - digit[i]
			if sum(thisScount.itervalues()) > 0:
				s = getDigits(Counter(thisScount), i)
				if s is not None:
					num = str(i) + str(s)
					return num
			else:
				return str(i)
		i += 1
	if len(num) != sum(scount.itervalues()):
		return None


def contains(a, b):
	return all(a[x] >= b[x] for x in b)

with open(sys.argv[2]) as inf:
	lines = inf.readlines()
	lines = [l.strip('\n') for l in lines]

outName = sys.argv[1] + "Output.txt"
ouf = open(outName, 'w')
for i in range(1, int(lines[0]) + 1):
	ouf.write("Case" + " #" + str(i) + ": " + getDigits(Counter(lines[i]), 0) + "\n")