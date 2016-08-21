t = int(raw_input())
for case in xrange(t):
	number = raw_input()

	stuff = [0 for i in xrange(10)]
	stuff[0] = number.count('Z')
	stuff[2] = number.count('W')
	stuff[4] = number.count('U')
	stuff[5] = number.count('F') - stuff[4]
	stuff[6] = number.count('X')
	stuff[8] = number.count('G')
	stuff[3] = number.count('H') - stuff[8]
	stuff[9] = number.count('I') - stuff[8] - stuff[6] - stuff[5]
	stuff[1] = number.count('O') - stuff[0] - stuff[2] - stuff[4]
	stuff[7] = number.count('V') - stuff[5]
	
	out = ""
	for i in xrange(10):
		if stuff[i] > 0:
			out += (str(i) * stuff[i])
	print "Case #"+str(case+1)+": "+out		
