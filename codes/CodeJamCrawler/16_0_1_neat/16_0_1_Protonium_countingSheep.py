infile = open('bottrust.in')
outfile = open('bottrust.out', 'w')

T = int(infile.readline().strip())

for i in xrange(T):
	check_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	instructions = infile.readline().strip().split()
	N = int(instructions[0])
	instructions = instructions[1:]

	M = N
	ori_list = sorted(set([int(k) for k in str(N)]))
	count = 1
	go = True

	while go:
		ori_list = sorted(set(ori_list + sorted(set([int(j) for j in str(N)]))))
		if N == 0:
			b = 'INSOMNIA'
			outfile.write('Case #%d: %s\n' % (i + 1, b))
			go = False
			continue
		elif ori_list == check_list:
			outfile.write('Case #%d: %d\n' % (i + 1, N))
			go = False
		else:
			N += M
			count += 1

	