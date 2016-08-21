import string

infile = 'input.in'

lines = [line.rstrip('\n') for line in open(infile, 'r')]

T = int(lines[0])
out = None

teststart = 1
linespercase = 2


for t in range(1, T + 1):

	out = ''

	testcase = lines[t] #list(map(int, lines[t].split(' ')))

	N = int(lines[teststart])
	P = [int(x) for x in lines[teststart+1].split()]
	parties = list(string.ascii_uppercase[:N])

	curr_state = {party:P[i] for i, party in enumerate(parties)}
	n = sum(curr_state.values())

	while True:

		first_max, sec_max = (0, None), (0, None)

		for p in curr_state:
			if curr_state[p] > first_max[0]: first_max = (curr_state[p], p)

		for p in curr_state:
			if curr_state[p] > sec_max[0] and p != first_max[1]: sec_max = (curr_state[p], p)

		if first_max[0] == 0: break

		if first_max[0] - sec_max[0] >= 2:
			out += 2*first_max[1] + ' '
			curr_state[first_max[1]] -= 2
			n -= 2
			continue


		if first_max[0] == 1 and sec_max[0] == 1 and n == 3:
			out += first_max[1] + ' '
			curr_state[first_max[1]] -= 1
			n -= 1
			continue

		if first_max[0] == 1 and sec_max[0] == 1 and (n == 2 or n > 3):
			out += first_max[1]+sec_max[1] + ' '
			curr_state[first_max[1]] -= 1
			curr_state[sec_max[1]] -= 1
			n -= 2
			continue

		if first_max[0] - sec_max[0] == 1:
			out += first_max[1] + ' '
			curr_state[first_max[1]] -= 1
			n -= 1
			continue

		if first_max[0] == sec_max[0]:
			out += first_max[1]+sec_max[1] + ' '
			curr_state[first_max[1]] -= 1
			curr_state[sec_max[1]] -= 1
			n -= 2
			continue
		

		break

	teststart += linespercase

	out = out[:-1]


	print('Case #{case}: {out}'.format(case=t, out=out))