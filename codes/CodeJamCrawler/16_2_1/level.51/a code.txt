from collections import Counter

for tc in range(input()):
	letters = list(raw_input())
	numbers = []
	for i in range(letters.count('Z')):
		letters.remove('Z')
		letters.remove('E')
		letters.remove('R')
		letters.remove('O')
		numbers.append("0")
	for i in range(letters.count('W')):
		letters.remove('T')
		letters.remove('W')
		letters.remove('O')
		numbers.append("2")
	for i in range(letters.count('X')):
		letters.remove('S')
		letters.remove('I')
		letters.remove('X')
		numbers.append("6")
	for i in range(letters.count('S')):
		letters.remove('S')
		letters.remove('E')
		letters.remove('V')
		letters.remove('E')
		letters.remove('N')
		numbers.append("7")
	for i in range(letters.count('V')):
		letters.remove('F')
		letters.remove('I')
		letters.remove('V')
		letters.remove('E')
		numbers.append("5")
	for i in range(letters.count('F')):
		letters.remove('F')
		letters.remove('O')
		letters.remove('U')
		letters.remove('R')
		numbers.append("4")
	for i in range(letters.count('G')):
		letters.remove('E')
		letters.remove('I')
		letters.remove('G')
		letters.remove('H')
		letters.remove('T')
		numbers.append("8")
	for i in range(letters.count('H')):
		letters.remove('T')
		letters.remove('H')
		letters.remove('R')
		letters.remove('E')
		letters.remove('E')
		numbers.append("3")
	for i in range(letters.count('I')):
		letters.remove('N')
		letters.remove('I')
		letters.remove('N')
		letters.remove('E')
		numbers.append("9")
	for i in range(letters.count('O')):
		letters.remove('O')
		letters.remove('N')
		letters.remove('E')
		numbers.append("1")
	numbers.sort()
	ans = ''.join(numbers)
	print "Case #" + str(tc + 1) + ": " + ans
