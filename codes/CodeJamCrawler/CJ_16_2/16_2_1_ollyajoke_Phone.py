def findNumber(s):
	number = []
	while len(s) > 0:
		if 'Z' in s:
			number.append('0')
			s.remove('Z')
			s.remove('E')
			s.remove('R')
			s.remove('O')
		elif 'W' in s:
			number.append('2')
			s.remove('T')
			s.remove('W')
			s.remove('O')
		elif 'U' in s:
			number.append('4')
			s.remove('F')
			s.remove('O')
			s.remove('U')
			s.remove('R')
		elif 'X' in s:
			number.append('6')
			s.remove('S')
			s.remove('I')
			s.remove('X')
		elif 'G' in s:
			number.append('8')
			s.remove('E')
			s.remove('I')
			s.remove('G')
			s.remove('H')
			s.remove('T')
		elif 'O' in s and 'N' in s:
			number.append('1')
			s.remove('N')
			s.remove('E')
			s.remove('O')	
		elif 'T' in s and 'R' in s:
			number.append('3')
			s.remove('T')
			s.remove('R')
			s.remove('E')
			s.remove('H')
			s.remove('E')
		elif 'F' in s and 'V' in s:
			number.append('5')
			s.remove('F')
			s.remove('I')
			s.remove('V')
			s.remove('E')
		elif 'N' in s and 'I' in s:
			number.append('9')
			s.remove('N')
			s.remove('I')
			s.remove('N')
			s.remove('E')	
		elif 'S' in s and 'V' in s:
			number.append('7')
			s.remove('S')
			s.remove('V')
			s.remove('E')
			s.remove('N')
			s.remove('E')
	number.sort()
	
	return "".join(number)			


T = int(raw_input().strip())
for i in range(0, T):
	s = raw_input().strip()
	print 'Case #' + str(i+1) + ':', findNumber(list(s))

# findNunber(list('OZONETOWER'))
# findNunber(list('WEIGHFOXTOURIST'))
# findNunber(list('OURNEONFOE'))
# findNunber(list('ETHER'))