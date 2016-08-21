
s = 'WEIGHFOXTOURIST'


def stripDigit(s, digit):
	s_list = list(s)
	for c in digit:
		pos = s.find(c)
		assert(pos != -1)
		del s_list[pos]
		s = ''.join(s_list)
	return s

def findNumbers(s):
	numbers = []

	while s.find('Z') != -1:
		s = stripDigit(s, 'ZERO')
		numbers.append(0)

	while s.find('W') != -1:
		s = stripDigit(s, 'TWO')
		numbers.append(2)

	while s.find('U') != -1:
		s = stripDigit(s, 'FOUR')
		numbers.append(4)

	while s.find('X') != -1:
		s = stripDigit(s, 'SIX')
		numbers.append(6)

	while s.find('G') != -1:
		s = stripDigit(s, 'EIGHT')
		numbers.append(8)

	while s.find('F') != -1:
		s = stripDigit(s, 'FIVE')
		numbers.append(5)

	# Not unique from here
	while s.find('H') != -1:
		s = stripDigit(s, 'THREE')
		numbers.append(3)

	while s.find('V') != -1:
		s = stripDigit(s, 'SEVEN')
		numbers.append(7)

	while s.find('O') != -1:
		s = stripDigit(s, 'ONE')
		numbers.append(1)

	while s.find('I') != -1:
		s = stripDigit(s, 'NINE')
		numbers.append(9)

	return numbers


filename = 'A-large'
f_out = open(filename + '.out', 'w')
with open(filename + '.in') as f_in:
	T = int(f_in.readline())
	for t in xrange(T):
		s = f_in.readline()
		numbers = findNumbers(s)
		numbers.sort()
		f_out.write('Case #' + str(t+1) + ': ')
		for n in numbers:
			f_out.write(str(n))
		f_out.write('\n')

f_out.close()


