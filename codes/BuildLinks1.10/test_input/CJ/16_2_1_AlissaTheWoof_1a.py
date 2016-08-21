t = int(input())

f = open('1aresult.txt', 'r+')

for a in range(1, t+1):
	total = 0
	in_file = list(raw_input())
	
	zeros = (in_file.count("Z"))
	for x in range(0, zeros):
		in_file.remove("Z")
		in_file.remove("E")
		in_file.remove("R")
		in_file.remove("O")

	twos = (in_file.count("W"))
	for x in range(0, twos):
		in_file.remove("T")
		in_file.remove("W")
		in_file.remove("O")


	fours = (in_file.count("U"))
	for x in range(0, fours):
		in_file.remove("F")
		in_file.remove("O")
		in_file.remove("U")
		in_file.remove("R")



	ones = (in_file.count("O"))
	for x in range(0, ones):
		in_file.remove("O")
		in_file.remove("N")
		in_file.remove("E")



	threes = (in_file.count("R"))
	for x in range(0, threes):
		in_file.remove("T")
		in_file.remove("H")
		in_file.remove("R")
		in_file.remove("E")
		in_file.remove("E")



	eights = (in_file.count("G"))
	for x in range(0, eights):
		in_file.remove("E")
		in_file.remove("I")
		in_file.remove("G")
		in_file.remove("H")
		in_file.remove("T")




	sixs = (in_file.count("X"))
	for x in range(0, sixs):
		in_file.remove("S")
		in_file.remove("I")
		in_file.remove("X")



	fives = (in_file.count("F"))
	for x in range(0, fives):
		in_file.remove("F")
		in_file.remove("I")
		in_file.remove("V")
		in_file.remove("E")





	sevens = (in_file.count("V"))
	for x in range(0, sevens):
		in_file.remove("S")
		in_file.remove("E")
		in_file.remove("V")
		in_file.remove("E")
		in_file.remove("N")


	nines = len(in_file)/4

	f.write("Case #" + str(a) + ": " + "0" * zeros + "1" * ones + "2" * twos
		+ "3" * threes + "4" * fours + "5" * fives + "6" * sixs + "7" * sevens + "8" * eights + "9" * nines +"\n")