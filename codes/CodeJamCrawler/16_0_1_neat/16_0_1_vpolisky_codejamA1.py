infile = 'input'

lines = [line.rstrip('\n') for line in open(infile, 'r')]

T = int(lines[0])

for t in range(1, T + 1):

	digits = ['0', '1', '3', '4', '5', '6', '7', '8', '9']

	N = int(lines[t])

	if N == 0:
		print('Case #{case}: INSOMNIA'.format(case=t))
		continue

	i = 0

	while True:

		i += 1
		n = str(i*N)

		for d in n:
			if d in digits: digits.remove(d)
			if not digits: break

		if not digits:
			print('Case #{case}: {last}'.format(case=t, last=n))
			break

	if digits: print('Case #{case}: INSOMNIA'.format(case=t))