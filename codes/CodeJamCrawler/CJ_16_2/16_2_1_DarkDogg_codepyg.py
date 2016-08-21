import sys
n = int(input())
for i in range(n):
	line = sys.stdin.readline()
	list1 = []
	while "Z" in line:
		line = line.replace("Z","",1)
		line = line.replace("E","",1)
		line = line.replace("R","",1)
		line = line.replace("O","",1)
		list1.append(0)
	while "W" in line:
		line = line.replace("T","",1)
		line = line.replace("W","",1)
		line = line.replace("O","",1)
		list1.append(2)
	while "U" in line:
		line = line.replace("F","",1)
		line = line.replace("O","",1)
		line = line.replace("U","",1)
		line = line.replace("R","",1)
		list1.append(4)
	while "X" in line:
		line = line.replace("S","",1)
		line = line.replace("I","",1)
		line = line.replace("X","",1)
		list1.append(6)
	while "O" in line and "N" in line and "E" in line:
		line = line.replace("O","",1)
		line = line.replace("N","",1)
		line = line.replace("E","",1)
		list1.append(1)
	while "N" in line and line.count("N")>=2 and "I" in line and "E" in line:
		line = line.replace("N","",2)
		line = line.replace("I","",1)
		line = line.replace("E","",1)
		list1.append(9)
	while "T" in line and "H" in line and "R" in line and "E" in line and line.count("E")>=2:
		line = line.replace("T","",1)
		line = line.replace("H","",1)
		line = line.replace("R","",1)
		line = line.replace("E","",2)
		list1.append(3)
	while "E" in line and "I" in line and "G" in line and "H" in line and "T" in line:
		line = line.replace("E","",1)
		line = line.replace("I","",1)
		line = line.replace("G","",1)
		line = line.replace("H","",1)
		line = line.replace("T","",1)
		list1.append(8)
	while "F" in line and "V" in line and "I" in line and "E" in line:
		line = line.replace("F","",1)
		line = line.replace("I","",1)
		line = line.replace("V","",1)
		line = line.replace("E","",1)
		list1.append(5)
	while "S" in line and "E" in line and line.count("E")>=2 and "V" in line and "N" in line:
		line = line.replace("S","",1)
		line = line.replace("E","",2)
		line = line.replace("V","",1)
		line = line.replace("N","",1)
		list1.append(7)
	list1.sort()
	l = "".join(map(str,list1))
	print("Case #%d: %s" % (i+1, l))