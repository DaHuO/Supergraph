import math
import random


def solve(b, m):

	matrix = [[0 for x in range(b)] for x in range(b)]

	maxi = 2**(b-2)
	if m > maxi:
		return ("IMPOSSIBLE", None)

	index = 0
	while m > 0:
		index += 1
		while int(math.ceil(float(maxi) / (2**index))) > m:
			index += 1
		m -= int(math.ceil(float(maxi) / (2**index)))
		matrix[0][index] = 1

		for j in range(index, b):
			for i in range(j+1, b):
				matrix[j][i] = 1


	return ("POSSIBLE", matrix)


name = "B-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	line = map(int, line)
	b = line[0]
	m = line[1]

	result = solve(b, m)
	fout.write("Case #" + str(i + 1) + ": " + result[0] + "\n")
	if result[1]:
		for row in result[1]:
			row = map(str, row)
			fout.write("".join(row) + "\n")
	print "Case #" + str(i + 1) + ": " + result[0]
	if result[1]:
		for row in result[1]:
			row = map(str, row)
			print "".join(row) + "\n",

fi.close()
fout.close()