import math
import random


def fillIn(a, liste):

	if not "?" in a:
		liste.append("".join(a))
	else:
		i = a.index("?")
		for b in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			acopy = a[:]
			acopy[i] = b
			fillIn(acopy, liste)

def solve(c, j):
	length = len(c)
	c = list(c)
	j = list(j)

	# for i in len(c):
	# 	if c[i] == "?" and j[i] == "?":
	# 		c[i] = ["0"]
	# 		j[i] = ["0"]
	# 	elif c[i] == "?" and j[i] != "?":
	# 		c[i] = j[i]
	# 	elif c[i] != "?" and j[i] == "?":
	# 		j[i] = c[i]

	listec = []
	fillIn(c, listec)
	listej = []
	fillIn(j, listej)
	listec = map(int, listec)
	listej = map(int, listej)

	minDiff = 999
	bestC = bestJ = 0
	for a in listec:
		for b in listej:
			if abs(b - a) < minDiff:
				minDiff = abs(b - a)
				bestC = a
				bestJ = b

	bestC = str(bestC)
	for i in range(length - len(bestC)):
		bestC = "0" + bestC

	bestJ = str(bestJ)
	for i in range(length - len(bestJ)):
		bestJ = "0" + bestJ

	return bestC + " " + bestJ

	


name = "B-small-attempt0"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	#line = map(int, line)
	c = line[0]
	j = line[1]

	result = str(solve(c,j))
	fout.write("Case #" + str(i + 1) + ": " + result + "\n")
	print "Case #" + str(i + 1) + ": " + result

fi.close()
fout.close()