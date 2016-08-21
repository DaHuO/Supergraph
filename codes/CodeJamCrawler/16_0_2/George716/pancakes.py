def change(l):
	l2 = []
	for p in l:
		if p == '+':
			l2.append('-')
		else:
			l2.append('+')
	return l2


def turn(l, ind):
	l1 = l[:ind]
	l2 = l[ind:]
	l1 = change(l1)

	return l1 + l2


f = open('input.txt')
line = f.readline().split()
num_test_cases = int(line[0])
results = []

for i in xrange(num_test_cases):
	pcks = []

	line = f.readline().split()
	s = line[0]

	for c in s:
		pcks.append(c)

	siz = len(pcks)

	if siz == 1:
		if pcks[0] == '+':
			results.append("Case #" + str(i + 1) + ": " + str(0) + '\n')
		else:
			results.append("Case #" + str(i + 1) + ": " + str(1) + '\n')
	else:
		done = False
		count = 0

		while not done:
			if pcks[0] == '+' and pcks[1] == '-':
				pcks[0] = '-'
				count += 1			
			else:
				num_in_correct_down = 0
				for pck in reversed(pcks):
					if(pck == '+'):
						num_in_correct_down += 1
					else:
						break

				if num_in_correct_down == siz:
					done = True
				else:
					ind = siz - num_in_correct_down
					pcks = turn(pcks, ind)
					count += 1
		results.append("Case #" + str(i + 1) + ": " + str(count) + '\n')

f2 = open('output.txt','w')
for i in xrange(num_test_cases):
	f2.write(results[i])