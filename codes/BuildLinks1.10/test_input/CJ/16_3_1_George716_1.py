f = open('input.txt')

line = f.readline().split()
num_test_cases = int(line[0])
results = []

letters = dict()
letters['A'] = 1
letters['B'] = 2
letters['C'] = 3
letters['D'] = 4
letters['E'] = 5
letters['F'] = 6
letters['G'] = 7
letters['H'] = 8
letters['I'] = 9
letters['J'] = 10
letters['K'] = 11
letters['L'] = 12
letters['M'] = 13
letters['N'] = 14
letters['O'] = 15
letters['P'] = 16
letters['Q'] = 17
letters['R'] = 18
letters['S'] = 19
letters['T'] = 20
letters['U'] = 21
letters['V'] = 22
letters['W'] = 23
letters['X'] = 24
letters['Y'] = 25
letters['Z'] = 26

letters2 = dict()
letters2[1] = 'A'
letters2[2] = 'B'
letters2[3] = 'C'
letters2[4] = 'D'
letters2[5] = 'E'
letters2[6] = 'F'
letters2[7] = 'G'
letters2[8] = 'H'
letters2[9] = 'I'
letters2[10] = 'J'
letters2[11] = 'K'
letters2[12] = 'L'
letters2[13] = 'M'
letters2[14] = 'N'
letters2[15] = 'O'
letters2[16] = 'P'
letters2[17] = 'Q'
letters2[18] = 'R'
letters2[19] = 'S'
letters2[20] = 'T'
letters2[21] = 'U'
letters2[22] = 'V'
letters2[23] = 'W'
letters2[24] = 'X'
letters2[25] = 'Y'
letters2[26] = 'Z'

for i in xrange(num_test_cases):
	line = f.readline().split()
	num_parties = int(line[0])
	snd = []
	outs = []
	
	line = f.readline().split()

	for j in xrange(len(line)):
		num_senators = int(line[j])
		snd.append(num_senators)

	finished = False
	while not finished:
		maxim = 0
		maxpos = 0


		for j in xrange(len(snd)):
			if maxim < snd[j]:
				maxim = snd[j]
				maxpos = j

		snd[maxpos] -= 1
		if len(outs) > 0:
					outs.append(' ')
		outs.append(letters2[maxpos + 1])

		sum_in = 0

		for j in xrange(len(snd)):
			sum_in += snd[j]
		for j in xrange(len(snd)):
			if snd[j] > 0.5 * sum_in:
				snd[j] -= 1
				outs.append(letters2[j + 1])
				

		finished = True
		for j in xrange(len(snd)):
			if snd[j] != 0:
				finished = False


	s = ''
	for j in xrange(len(outs)):
		s += outs[j]
	results.append("Case #" + str(i + 1) + ": " + s + '\n')


f2 = open('output.txt','w')
for i in xrange(num_test_cases):
	f2.write(results[i])