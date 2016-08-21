f = open("A-large.in", 'r')
g = open("output.out", 'w')
cases = int(f.readline())
i = 0

while i<cases:

  	i = i+1
 	string = f.readline()
 	s_list = list(string)
 	result = ''

 	zero = True
 	while zero:
	 	if 'Z' in s_list and 'E' in s_list and 'R' in s_list and 'O' in s_list:
	 		result = result + '0'
	 		for e in s_list:
				if e == 'Z':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'E':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'R':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'O':
					s_list.remove(e)
					break
		else:
			zero = False

	two = True
 	while two:
	 	if 'T' in s_list and 'W' in s_list and 'O' in s_list :
	 		result = result + '2'
	 		for e in s_list:
				if e == 'T':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'W':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'O':
					s_list.remove(e)
					break
		else:
			two = False

	six = True
 	while six:
	 	if 'S' in s_list and 'I' in s_list and 'X' in s_list :
	 		result = result + '6'
	 		for e in s_list:
				if e == 'S':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'I':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'X':
					s_list.remove(e)
					break
		else:
			six = False

	four = True
 	while four:
	 	if 'F' in s_list and 'O' in s_list and 'U' in s_list and 'R' in s_list:
	 		result = result + '4'
	 		for e in s_list:
				if e == 'F':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'O':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'U':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'R':
					s_list.remove(e)
					break
		else:
			four = False

	five = True
 	while five:
	 	if 'F' in s_list and 'I' in s_list and 'V' in s_list and 'E' in s_list:
	 		result = result + '5'
	 		for e in s_list:
				if e == 'F':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'I':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'V':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'E':
					s_list.remove(e)
					break
		else:
			five = False

	seven = True
 	while seven:
	 	if 'S' in s_list and 'V' in s_list and 'N' in s_list and s_list.count('E') > 1:
	 		result = result + '7'
	 		for e in s_list:
				if e == 'S':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'E':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'V':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'E':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'N':
					s_list.remove(e)
					break
		else:
			seven = False

	eight = True
 	while eight:
	 	if 'E' in s_list and 'I' in s_list and 'G' in s_list and 'H' in s_list and 'T' in s_list:
	 		result = result + '8'
	 		for e in s_list:
				if e == 'E':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'I':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'G':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'H':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'T':
					s_list.remove(e)
					break
		else:
			eight = False

	three = True
 	while three:
	 	if 'T' in s_list and 'H' in s_list and 'R' in s_list and s_list.count('E') > 1:
	 		result = result + '3'
	 		for e in s_list:
				if e == 'T':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'H':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'R':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'E':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'E':
					s_list.remove(e)
					break
		else:
			three = False

	nine = True
 	while nine:
	 	if s_list.count('N') > 1 and 'I' in s_list and 'E' in s_list:
	 		result = result + '9'
	 		for e in s_list:
				if e == 'N':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'I':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'N':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'E':
					s_list.remove(e)
					break
		else:
			nine = False

	one = True
 	while one:
	 	if 'O' in s_list and 'N' in s_list and 'E' in s_list :
	 		result = result + '1'
	 		for e in s_list:
				if e == 'O':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'N':
					s_list.remove(e)
					break
			for e in s_list:
				if e == 'E':
					s_list.remove(e)
					break
		else:
			one = False

	result = ''.join(sorted(result))

	g.write("Case #" + str(i) + ": " + result + "\n")





	
