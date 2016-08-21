def decipher_number(s):
	nletters = {}
	ndigits = {}
	for i in range(ord('A'), ord('Z')+1):
		nletters[chr(i)] = 0
	for i in xrange(0, 10):
		ndigits[i] = 0
	for c in s:
		nletters[c] += 1
	ndigits[0] = nletters['Z']
	ndigits[1] = nletters['O'] - nletters['Z'] - nletters['W'] - nletters['U']
	ndigits[2] = nletters['W']
	ndigits[3] = nletters['T'] - nletters['W'] - nletters['G']
	ndigits[4] = nletters['U']
	ndigits[5] = nletters['F'] - nletters['U']
	ndigits[6] = nletters['X']
	ndigits[7] = nletters['S'] - nletters['X']
	ndigits[8] = nletters['G']
	ndigits[9] = (nletters['N'] - ndigits[1] - ndigits[7])/2
	
	res = []
	for i in xrange(0, 10):
		for j in xrange(0, ndigits[i]):
			res.append(i)
	return ''.join(map(str, res))


inf = open("a.in", 'r')
outf = open("a.out", 'w')

t = int(inf.readline())

for k in xrange(0, t):
	s = inf.readline().strip()
	outf.write("Case #" + str(k + 1) + ": ")	
	outf.write(decipher_number(s) + "\n")
outf.close()
