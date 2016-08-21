#!/usr/bin/python
import sys


def findDigits(s):
	digits = []
	s= s.rstrip('\r\n')
	while s!='':
		pos = s.find('Z')
		while pos != -1:
			s = s[:pos] + s[(pos+1):]
			pos = s.find('E')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('R')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('O')
			s = s[:pos] + s[(pos+1):]
			digits.append('0')
			pos = s.find('Z')

		pos = s.find('X')
		while pos != -1:
			s = s[:pos] + s[(pos+1):]
			pos = s.find('I')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('S')
			s = s[:pos] + s[(pos+1):]
			digits.append('6')
			pos = s.find('X')

		pos = s.find('W')
		while pos != -1:
			s = s[:pos] + s[(pos+1):]
			pos = s.find('O')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('T')
			s = s[:pos] + s[(pos+1):]
			digits.append('2')
			pos = s.find('W')

		pos = s.find('G')
		while pos != -1:
			s = s[:pos] + s[(pos+1):]
			pos = s.find('E')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('I')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('T')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('H')
			s = s[:pos] + s[(pos+1):]
			digits.append('8')
			pos = s.find('G')

		pos = s.find('H')
		while pos != -1:
			s = s[:pos] + s[(pos+1):]
			pos = s.find('T')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('R')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('E')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('E')
			s = s[:pos] + s[(pos+1):]
			digits.append('3')
			pos = s.find('H')

		pos = s.find('R')
		while pos != -1:
			s = s[:pos] + s[(pos+1):]
			pos = s.find('F')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('O')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('U')
			s = s[:pos] + s[(pos+1):]
			digits.append('4')
			pos = s.find('R')

		pos = s.find('O')
		while pos != -1:
			s = s[:pos] + s[(pos+1):]
			pos = s.find('N')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('E')
			s = s[:pos] + s[(pos+1):]
			digits.append('1')
			pos = s.find('O')

		pos = s.find('F')
		while pos != -1:
			s = s[:pos] + s[(pos+1):]
			pos = s.find('I')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('V')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('E')
			s = s[:pos] + s[(pos+1):]
			digits.append('5')
			pos = s.find('F')

		pos = s.find('S')
		while pos != -1:
			s = s[:pos] + s[(pos+1):]
			pos = s.find('E')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('V')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('E')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('N')
			s = s[:pos] + s[(pos+1):]
			digits.append('7')
			pos = s.find('S')

		pos = s.find('N')
		while pos != -1:
			s = s[:pos] + s[(pos+1):]
			pos = s.find('I')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('N')
			s = s[:pos] + s[(pos+1):]
			pos = s.find('E')
			s = s[:pos] + s[(pos+1):]
			digits.append('9')
			pos = s.find('N')

		print digits
		print '%s....'%s
		print len(s)


	return digits



if __name__ == '__main__':
	input = open(sys.argv[1])
	output = open(sys.argv[1]+'.out', 'w')

	nTestCases = int(input.readline())
	for t in range(0, nTestCases):
		s = input.readline()
		digits = findDigits(s)
		print digits

		output.write('Case #%i: %s\n'%(int(t+1), "".join(sorted(digits))))
	input.close()
	output.close()
