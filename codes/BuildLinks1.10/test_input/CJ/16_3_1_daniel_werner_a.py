import math
import random

names = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def solve(parties):

	strat = []
	while sum(parties) > 0:
		result = ""
		first = parties.index(max(parties))
		parties[first] -= 1
		result += names[first]
		if sum(parties) != 2:
			second = parties.index(max(parties))
			parties[second] -= 1
			result += names[second]

		strat.append(result)

	return " ".join(strat)



name = "A-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	line2 = fi.readline().strip().split(" ")
	line2 = map(int, line2)

	result = str(solve(line2))
	fout.write("Case #" + str(i + 1) + ": " + result + "\n")
	print "Case #" + str(i + 1) + ": " + result

fi.close()
fout.close()