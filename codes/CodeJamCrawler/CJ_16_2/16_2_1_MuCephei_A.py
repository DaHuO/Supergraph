def Remove0(string):
	if 'Z' in string:
		string.remove('Z')
		string.remove('E')
		string.remove('R')
		string.remove('O')
		return True
	return False

def Remove1(string):
	if 'O' in string:
		string.remove('O')
		string.remove('N')
		string.remove('E')
		return True
	return False

def Remove2(string):
	if 'W' in string:
		string.remove('T')
		string.remove('W')
		string.remove('O')
		return True
	return False

def Remove3(string):
	if 'T' in string:
		string.remove('T')
		string.remove('H')
		string.remove('R')
		string.remove('E')
		string.remove('E')
		return True
	return False

def Remove4(string):
	if 'R' in string:
		string.remove('F')
		string.remove('O')
		string.remove('U')
		string.remove('R')
		return True
	return False

def Remove5(string):
	if 'F' in string:
		string.remove('F')
		string.remove('I')
		string.remove('V')
		string.remove('E')
		return True
	return False

def Remove6(string):
	if 'X' in string:
		string.remove('S')
		string.remove('I')
		string.remove('X')
		return True
	return False

def Remove7(string):
	if 'V' in string:
		string.remove('S')
		string.remove('E')
		string.remove('V')
		string.remove('E')
		string.remove('N')
		return True
	return False

def Remove8(string):
	if 'G' in string:
		string.remove('E')
		string.remove('I')
		string.remove('G')
		string.remove('H')
		string.remove('T')
		return True
	return False

def Remove9(string):
	if 'N' in string:
		string.remove('N')
		string.remove('I')
		string.remove('N')
		string.remove('E')
		return True
	return False

def A(string):
	inputstring = []
	for letter in string:
		inputstring.append(letter)
	phone = []
	while Remove0(inputstring):
		phone.append(0)

	while Remove2(inputstring):
		phone.append(2)

	while Remove6(inputstring):
		phone.append(6)

	while Remove8(inputstring):
		phone.append(8)

	while Remove3(inputstring):
		phone.append(3)

	while Remove4(inputstring):
		phone.append(4)

	while Remove5(inputstring):
		phone.append(5)

	while Remove7(inputstring):
		phone.append(7)

	while Remove1(inputstring):
		phone.append(1)

	while Remove9(inputstring):
		phone.append(9)

	phone.sort()


	return toString(phone)


def toString(data):
	result = ""
	for x in data:
		result = result + str(x)
	return result


times = input()

for x in range(times):
    print ("Case #" + str(x+1) + ": " + A(str(raw_input())))