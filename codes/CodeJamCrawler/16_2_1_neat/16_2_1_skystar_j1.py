f = open("D:\python\input.txt",'r')
t = int(f.readline())

s=''
n=0

digit = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

res = []
allres = []

for i in range(t):
	s = list(f.readline().replace("\n",''))
	if "Z" in s:
		c = s.count("Z")
		for j in range(c):
			s.remove("Z")
			s.remove("E")
			s.remove("R")
			s.remove("O")
			res.append("0")
	if "W" in s:
		c = s.count("W")
		for j in range(c):
			s.remove("T")
			s.remove("W")
			s.remove("O")
			res.append("2")
	if "U" in s:
		c = s.count("U")
		for j in range(c):
			s.remove("F")
			s.remove("O")
			s.remove("R")
			s.remove("U")
			res.append("4")
	if "X" in s:
		c = s.count("X")
		for j in range(c):
			s.remove("S")
			s.remove("I")
			s.remove("X")
			res.append("6")
	if "G" in s:
		c = s.count("G")
		for j in range(c):
			s.remove("E")
			s.remove("I")
			s.remove("G")
			s.remove("H")
			s.remove("T")
			res.append("8")
	if "F" in s:
		c = s.count("F")
		for j in range(c):
			s.remove("F")
			s.remove("I")
			s.remove("V")
			s.remove("E")
			res.append("5")
	if "I" in s:
		c = s.count("I")
		for j in range(c):
			s.remove("N")
			s.remove("I")
			s.remove("N")
			s.remove("E")
			res.append("9")
	if "V" in s:
		c = s.count("V")
		for j in range(c):
			s.remove("S")
			s.remove("E")
			s.remove("V")
			s.remove("E")
			s.remove("N")
			res.append("7")
	if "H" in s:
		c = s.count("H")
		for j in range(c):
			s.remove("T")
			s.remove("H")
			s.remove("R")
			s.remove("E")
			s.remove("E")
			res.append("3")
	if "O" in s:
		c = s.count("O")
		for j in range(c):
			s.remove("O")
			s.remove("N")
			s.remove("E")
			res.append("1")
	res.sort()
	allres.append("Case #" + str(len(allres)+1) + ": " + ''.join(res))
	res.clear()

f.close()

f = open("D:\python\output.txt",'w')
f.write('\n'.join(allres))
f.close()