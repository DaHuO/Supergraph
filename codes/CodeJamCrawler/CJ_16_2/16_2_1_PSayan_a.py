t = input()
s = [raw_input() for _ in xrange(t)]
for i in xrange(len(s)):
	p = list(s[i])
	num = ""
	d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
	#print p
	temp = list(p)
	for c in temp:
		if c == 'Z':
			#print c
			d[0] += 1
			p.remove('Z')
			p.remove('E')
			p.remove('R')
			p.remove('O')
			#print p
		elif c == 'W':
			#print c
			d[2] += 1
			p.remove('T')
			p.remove('W')
			p.remove('O')
			#print p
		elif c == 'U':
			#print c
			d[4] += 1
			p.remove('F')
			p.remove('O')
			p.remove('U')
			p.remove('R')
			#print p
		elif c == 'X':
			#print c
			d[6] += 1
			p.remove('S')
			p.remove('I')
			p.remove('X')
			#print p
		elif c == 'G':
			#print c
			d[8] += 1
			p.remove('E')
			p.remove('I')
			p.remove('G')
			p.remove('H')
			p.remove('T')
			#print p
	temp = list(p)
	for c in temp:
		if c == 'T':
			#print c
			d[3] += 1
			p.remove('T')
			p.remove('H')
			p.remove('R')
			p.remove('E')
			p.remove('E')
			#print p
		elif c == 'O':
			d[1] += 1
			p.remove('O')
			p.remove('N')
			p.remove('E')
			#print p
		elif c == 'F':
			d[5] += 1
			p.remove('F')
			p.remove('I')
			p.remove('V')
			p.remove('E')
		elif c == 'S':
			d[7] += 1
			p.remove('S')
			p.remove('E')
			p.remove('V')
			p.remove('E')
			p.remove('N')
	d[9] += p.count('I')
	#print d
	for j in xrange(10):
		if d[j] != 0:
			num += str(j) * d[j]
	print "Case #" + str(i + 1) + ": " + num
