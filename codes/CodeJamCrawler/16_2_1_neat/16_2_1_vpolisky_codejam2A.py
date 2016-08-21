infile = 'input.in'

lines = [line.rstrip('\n') for line in open(infile, 'r')]

T = int(lines[0])
out = None

teststart = 1
linespercase = 1

letter_dict = {
	0: 'ZERO',
	1: 'ONE',
	2: 'TWO',
	3: 'THREE',
	4: 'FOUR',
	5: 'FIVE',
	6: 'SIX',
	7: 'SEVEN',
	8: 'EIGHT',
	9: 'NINE',
}

letters = ''

for d in letter_dict.values():
	for l in d:
		if l not in letters:
			letters += l


digits_dict = {l: 0 for l in letters}

def del_char(s, c):
	p = s.index(c)
	s = s[:p] + s[p+1:]
	return s

for t in range(1, T + 1):

	testcase = lines[t] #list(map(int, lines[t].split(' ')))

	digits = {i: 0 for i in range(10)}

	for l in testcase:
		digits_dict[l] += 1

	for l in testcase:

		if l == 'Z':
			digits[0] += 1
			for c in letter_dict[0]:
				testcase = del_char(testcase, c)

		if l == 'W':
			digits[2] += 1
			for c in letter_dict[2]:
				testcase = del_char(testcase, c)

		if l == 'U':
			digits[4] += 1
			for c in letter_dict[4]:
				testcase = del_char(testcase, c)

		if l == 'X':
			digits[6] += 1
			for c in letter_dict[6]:
				testcase = del_char(testcase, c)

		if l == 'G':
			digits[8] += 1
			for c in letter_dict[8]:
				testcase = del_char(testcase, c)
	
	for l in testcase:

		if l == 'O':
			digits[1] += 1
			for c in letter_dict[1]:
				testcase = del_char(testcase, c)

		if l == 'T':
			digits[3] += 1
			for c in letter_dict[3]:
				testcase = del_char(testcase, c)

		if l == 'F':
			digits[5] += 1
			for c in letter_dict[5]:
				testcase = del_char(testcase, c)

		if l == 'S':
			digits[7] += 1
			for c in letter_dict[7]:
				testcase = del_char(testcase, c)

	digits[9] = len(testcase)//4

	out = ''

	for d in digits:
		out = out + str(d)*digits[d]

	print('Case #{case}: {out}'.format(case=t, out=out))
	out = ''