import os

input_file = open("input_large.in", "r")
output_file = open("output_large.txt", "w")

cases = int(input_file.readline())

for i in range(cases):
	word = list(input_file.readline())[:-1]
	digits = []
	
	# Find zeros
	while "Z" in word:
		word.remove("Z")
		word.remove("E")
		word.remove("R")
		word.remove("O")
		digits.append(0)

	while "X" in word:
		word.remove("S")
		word.remove("I")
		word.remove("X")
		digits.append(6)

	while "G" in word:
		word.remove("E")
		word.remove("I")
		word.remove("G")
		word.remove("H")
		word.remove("T")
		digits.append(8)

	while "S" in word:
		word.remove("S")
		word.remove("E")
		word.remove("V")
		word.remove("E")
		word.remove("N")
		digits.append(7)

	while "V" in word:
		word.remove("F")
		word.remove("I")
		word.remove("V")
		word.remove("E")
		digits.append(5)

	while "I" in word:
		word.remove("N")
		word.remove("I")
		word.remove("N")
		word.remove("E")
		digits.append(9)

	while "F" in word:
		word.remove("F")
		word.remove("O")
		word.remove("U")
		word.remove("R")
		digits.append(4)

	while "N" in word:
		word.remove("O")
		word.remove("N")
		word.remove("E")
		digits.append(1)

	while "W" in word:
		word.remove("T")
		word.remove("W")
		word.remove("O")
		digits.append(2)

	while "T" in word:
		word.remove("T")
		word.remove("H")
		word.remove("R")
		word.remove("E")
		word.remove("E")
		digits.append(3)

	digits.sort()
	output = [str(d) for d in digits]
	output = "".join(output)

	output_file.write("Case #" + str(i+1) + ": " + output + "\n")