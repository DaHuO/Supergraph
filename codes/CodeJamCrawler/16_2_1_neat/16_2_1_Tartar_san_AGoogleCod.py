f = open("A-large.in" , "r")
lines = f.readlines()
f.close()
f = open("result.txt", "w")
for i in range(1, len(lines)):
	numbers = [0 for i in range(10)]
	line = [letter for letter in lines[i]]
	while "Z" in line:
		line.remove("Z")
		line.remove("E")
		line.remove("R")
		line.remove("O")
		numbers[0] += 1
	while "W" in line:
		line.remove("T")
		line.remove("W")
		line.remove("O")
		numbers[2] += 1
	while "U" in line:
		line.remove("F")
		line.remove("O")
		line.remove("U")
		line.remove("R")
		numbers[4] += 1
	while "X" in line:
		line.remove("S")
		line.remove("I")
		line.remove("X")
		numbers[6] += 1
	while "G" in line:
		line.remove("E")
		line.remove("I")
		line.remove("G")
		line.remove("H")
		line.remove("T")
		numbers[8] += 1
	while "O" in line:
		line.remove("O")
		line.remove("N")
		line.remove("E")
		numbers[1] += 1
	while "H" in line:
		line.remove("T")
		line.remove("H")
		line.remove("R")
		line.remove("E")
		line.remove("E")
		numbers[3] += 1
	while "F" in line:
		line.remove("F")
		line.remove("I")
		line.remove("V")
		line.remove("E")
		numbers[5] += 1
	while "S" in line:
		line.remove("S")
		line.remove("E")
		line.remove("V")
		line.remove("E")
		line.remove("N")
		numbers[7] += 1
	while "N" in line:
		line.remove("N")
		line.remove("I")
		line.remove("N")
		line.remove("E")
		numbers[9] += 1
	result = ""
	for j in range(10):
		while(numbers[j] > 0):
			numbers[j] -= 1
			result += str(j)
	f.write("Case #" + str(i) + ": " + str(result) + "\n")
f.close()
