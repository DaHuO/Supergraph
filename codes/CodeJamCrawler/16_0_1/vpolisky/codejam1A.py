infile = 'input.in'

lines = [line.rstrip('\n') for line in open(infile, 'r')]

T = int(lines[0])
out = None


for t in range(1, T + 1):

	testcase = lines[t] #list(map(int, lines[t].split(' ')))

	letters = list(testcase)
	order = ''

	order = letters[0]

	for letter in letters[1:]:
		if letter >= order[0]:
			order = letter + order
		else:
			order = order + letter

	out = order
	print('Case #{case}: {out}'.format(case=t, out=out))