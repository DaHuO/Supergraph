import math
import random

def generate(string, r, p, s):

	gotOne = False
	origString = string[:]
	if r+p+s == 0:
		while len(string) > 1:
			newString = ""
			for i in range(0, len(string), 2):
				if string[i:i+2] == "PR" or string[i:i+2] == "SP" or string[i:i+2] == "RS":
					newString += string[i]
				elif string[i:i+2] == "RP" or string[i:i+2] == "PS" or string[i:i+2] == "SR":
					newString += string[i+1]
				else:
					return False

			string = newString
		return origString

	if p:
		gotOne = generate(string + "P", r, p-1, s)
	if gotOne:
		return gotOne

	if r:
		gotOne = generate(string + "R", r-1, p, s)
	if gotOne:
		return gotOne

	if s:
		gotOne = generate(string + "S", r, p, s-1)

	return gotOne


def solve(n, r, p, s):

	a = generate("", r, p, s)
	if a:
		return a
	else:
		return "IMPOSSIBLE"



name = "A-small-attempt0"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	line = map(int, line)
	n = line[0]
	r = line[1]
	p = line[2]
	s = line[3]

	result = str(solve(n, r, p, s))
	fout.write("Case #" + str(i + 1) + ": " + result + "\n")
	print "Case #" + str(i + 1) + ": " + result

fi.close()
fout.close()