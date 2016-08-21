T = 0

def find_num(s, case_num):
	list_s = list(s)
	my_num = []
	while 'Z' in list_s:
		my_num.append("0")
		list_s.remove('Z')
		list_s.remove('E')
		list_s.remove('R')
		list_s.remove('O')
	while 'W' in list_s:
		my_num.append('2')
		list_s.remove('T')
		list_s.remove('W')
		list_s.remove('O')
	while 'G' in list_s:
		my_num.append('8')
		list_s.remove('E')
		list_s.remove('I')
		list_s.remove('G')
		list_s.remove('H')
		list_s.remove('T')
	while 'H' in list_s:
		my_num.append('3')
		list_s.remove('T')
		list_s.remove('H')
		list_s.remove('R')
		list_s.remove('E')
		list_s.remove('E')
	while 'U' in list_s:
		my_num.append('4')
		list_s.remove('F')
		list_s.remove('O')
		list_s.remove('U')
		list_s.remove('R')
	while 'X' in list_s:
		my_num.append('6')
		list_s.remove('S')
		list_s.remove('I')
		list_s.remove('X')	
	while 'V' in list_s:
		if 'S' in list_s:
			my_num.append('7')
			list_s.remove('S')
			list_s.remove('E')
			list_s.remove('V')
			list_s.remove('E')
			list_s.remove('N')
		else:
			my_num.append('5')
			list_s.remove('F')
			list_s.remove('I')
			list_s.remove('V')
			list_s.remove('E')	
	while 'O' in list_s:
		my_num.append('1')
		list_s.remove('O')
		list_s.remove('N')
		list_s.remove('E')
	while 'I' in list_s:
		my_num.append('9')
		list_s.remove('N')
		list_s.remove('I')
		list_s.remove('N')
		list_s.remove('E')
	my_num.sort()
	num = ''.join(my_num)
	print "Case #{}: {}".format(case_num, num)

T = int(raw_input())  # read a line with a single integer
for case_num in xrange(1, T + 1):
  s = raw_input()
  find_num(s, case_num)
  # check out .format's specification for more formatting options

