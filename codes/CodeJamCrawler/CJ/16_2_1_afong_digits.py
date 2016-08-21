from sys import argv

def charlesbarkleyscodejam(line):
	chars = []
	result = []
	for char in line:
		chars.append(char)
	#brute
	while 1:
		#print(''.join(chars))
		if 'Z' in chars:
			result.append(str(0))
			chars.remove('Z')
			chars.remove('E')
			chars.remove('R')
			chars.remove('O')
			continue
		if 'W' in chars:
			result.append(str(2))
			chars.remove('T')
			chars.remove('W')
			chars.remove('O')
			continue
		if 'U' in chars:
			result.append(str(4))
			chars.remove('F')
			chars.remove('O')
			chars.remove('U')
			chars.remove('R')
			continue
		if 'X' in chars:
			result.append(str(6))
			chars.remove('S')
			chars.remove('I')
			chars.remove('X')
			continue
		if 'G' in chars:
			result.append(str(8))
			chars.remove('E')
			chars.remove('I')
			chars.remove('G')
			chars.remove('H')
			chars.remove('T')
			continue
		if 'O' in chars:
			result.append(str(1))
			chars.remove('O')
			chars.remove('N')
			chars.remove('E')
			continue
		if 'F' in chars:
			result.append(str(5))
			chars.remove('F')
			chars.remove('I')
			chars.remove('V')
			chars.remove('E')
			continue
		if 'V' in chars:
			result.append(str(7))
			chars.remove('S')
			chars.remove('E')
			chars.remove('V')
			chars.remove('E')
			chars.remove('N')
			continue
		if 'T' in chars:
			result.append(str(3))
			chars.remove('T')
			chars.remove('H')
			chars.remove('R')
			chars.remove('E')
			chars.remove('E')
			continue
		if 'N' in chars:
			result.append(str(9))
			chars.remove('N')
			chars.remove('I')
			chars.remove('N')
			chars.remove('E')
			continue
		break
	result.sort()
	return(''.join(result))

with open(argv[1],'r') as file:
	lines = int(file.readline())
	for i, line in enumerate(file):
		print('Case #'+str(i+1)+': '+ charlesbarkleyscodejam(line.strip()))