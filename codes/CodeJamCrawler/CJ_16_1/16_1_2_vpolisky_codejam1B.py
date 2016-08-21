infile = 'input.in'

lines = [line.rstrip('\n') for line in open(infile, 'r')]

T = int(lines[0])
out = None

teststart = 1
linespercase = 0


for t in range(1, T + 1):

	testcase = lines[t] #list(map(int, lines[t].split(' ')))

	N = int(lines[teststart])
	linespercase = 2*N

	d = dict()
	missing = []

	for n in range(1, linespercase):
		
		h = [int(x) for x in lines[teststart+n].split(' ')]
		
		for x in h:
			if x not in d:
				d[x] = 1
			else:
				d[x] += 1


	for k in d:
		if d[k]%2 != 0:
			missing.append(k)

	missing.sort()

	out = ' '.join(str(x) for x in missing)




	teststart += linespercase


	print('Case #{case}: {out}'.format(case=t, out=out))