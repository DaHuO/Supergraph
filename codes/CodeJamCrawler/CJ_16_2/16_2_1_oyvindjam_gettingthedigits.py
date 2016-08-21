import sys

sys.stdin.readline()

f = open("output", "w")
for case, line in enumerate(sys.stdin, 1):
	line = list(line.strip())

	counts = [0] * 10
	index = 0;
	while True:
		if index >= len(line):
			break
		if line[index] == "Z":
			counts[0] += 1
			line.remove("Z")
			line.remove("E")
			line.remove("R")
			line.remove("O")
			index = 0
		elif line[index] == "W":
			counts[2] += 1
			line.remove("T")
			line.remove("W")
			line.remove("O")
			index = 0
		elif line[index] == "U":
			counts[4] += 1
			line.remove("F")
			line.remove("O")
			line.remove("U")
			line.remove("R")
			index = 0
		elif line[index] == "X":
			counts[6] += 1
			line.remove("S")
			line.remove("I")
			line.remove("X")
			index = 0
		elif line[index] == "G":
			index = 0
			counts[8] += 1
			line.remove("E")
			line.remove("I")
			line.remove("G")
			line.remove("H")
			line.remove("T")
			index = 0
		else:
			index += 1
	
	index = 0;
	while True:
		if index >= len(line):
			break

		if line[index] == "O":
			counts[1] += 1
			line.remove("O")
			line.remove("N")
			line.remove("E")
			index = 0
		elif line[index] == "T":
			counts[3] += 1
			line.remove("T")
			line.remove("H")
			line.remove("R")
			line.remove("E")
			line.remove("E")
			index = 0
		elif line[index] == "F":
			index = 0
			counts[5] += 1
			line.remove("F")
			line.remove("I")
			line.remove("V")
			line.remove("E")
			index = 0
		elif line[index] == "S":
			index = 0
			counts[7] += 1
			line.remove("S")
			line.remove("E")
			line.remove("V")
			line.remove("E")
			line.remove("N")
			index = 0
		else:
			index += 1

	counts[9] = len(line) / 4

	number = ""
	for digit, count in enumerate(counts):
		digit = str(digit)
		number += digit * count;

	f.write("Case #%d: %s\n" % (case, number)) 
	
