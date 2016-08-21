infile = 'input.in'

lines = [line.rstrip('\n') for line in open(infile, 'r')]

T = int(lines[0])


for t in range(1, T + 1):

	testcase = list(map(int, lines[t].split(' ')))
	K = int(testcase[0])
	C = int(testcase[1])
	S = int(testcase[2])

	if K == 1:
		print('Case #{case}: 1'.format(case=t))
		continue

	if C == 1:

		if S >= K:
			positions = ' '.join([str(pos) for pos in range(1, K+1)])
			print('Case #{case}: {positions}'.format(case=t, positions=positions))
		else:
			print('Case #{case}: IMPOSSIBLE'.format(case=t))

	else:

		if S >= K - 1:
			positions = ' '.join([str(pos) for pos in range(2, K+1)])
			print('Case #{case}: {positions}'.format(case=t, positions=positions))
		else:
			print('Case #{case}: IMPOSSIBLE'.format(case=t))