t = int(raw_input())
out = open('getting_the_digits_out.txt', 'w')
for i in xrange(t):
	s = raw_input()

	num = ''
	count = s.count('Z')
	for j in xrange(0, count):
		num += '0'
	s = s.replace('Z', '', count)
	s = s.replace('E', '', count)
	s = s.replace('R', '', count)
	s = s.replace('O', '', count)

	count = s.count('W')
	for j in xrange(0, count):
		num += '2'
	s = s.replace('T', '', count)
	s = s.replace('W', '', count)
	s = s.replace('O', '', count)

	count = s.count('X')
	for j in xrange(0, count):
		num += '6'
	s = s.replace('S', '', count)
	s = s.replace('I', '', count)
	s = s.replace('X', '', count)

	count = s.count('G')
	for j in xrange(0, count):
		num += '8'
	s = s.replace('E', '', count)
	s = s.replace('I', '', count)
	s = s.replace('G', '', count)
	s = s.replace('H', '', count)
	s = s.replace('T', '', count)

	count = s.count('T')
	for j in xrange(0, count):
		num += '3'
	s = s.replace('T', '', count)
	s = s.replace('H', '', count)
	s = s.replace('R', '', count)
	s = s.replace('E', '', 2 * count)

	count = s.count('R')
	for j in xrange(0, count):
		num += '4'
	s = s.replace('F', '', count)
	s = s.replace('O', '', count)
	s = s.replace('U', '', count)
	s = s.replace('R', '', count)

	count = s.count('O')
	for j in xrange(0, count):
		num += '1'
	s = s.replace('O', '', count)
	s = s.replace('N', '', count)
	s = s.replace('E', '', count)

	count = s.count('F')
	for j in xrange(0, count):
		num += '5'
	s = s.replace('F', '', count)
	s = s.replace('I', '', count)
	s = s.replace('V', '', count)
	s = s.replace('E', '', count)

	count = s.count('V')
	for j in xrange(0, count):
		num += '7'
	s = s.replace('S', '', count)
	s = s.replace('E', '', 2 * count)
	s = s.replace('V', '', count)
	s = s.replace('N', '', count)

	count = s.count('E')
	for j in xrange(0, count):
		num += '9'
	s = s.replace('N', '', 2 * count)
	s = s.replace('I', '', count)
	s = s.replace('E', '', count)

	out.write('Case #' + str(i + 1) + ': ' + ''.join(sorted(num)) + '\n')
out.close()