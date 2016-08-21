# counting sheep
outputfile = file('cs-big.out', 'w')
with open('A-large.in') as f:
	T = f.readline()[:-1]
	case = 1
	for N in f:
		# print N[-1:]
		if N[-1:] == '\n':
			N = int(N[:-1])
		else:
			N = int(N)
		# print 'N: ' + str(N)
		# print N
		if N < 1:
			outputfile.write( 'Case #' + str(case) + ': ' + 'INSOMNIA\n')
			case += 1
			continue
		z = 1
		x = 1
		numbers = []
		while True:
			N_map = map(int, str(N * x))
			# print N_map
			for i in N_map:
				# print i
				if i not in numbers:
					# print 'not in numbers: ' + str(i)
					numbers.append(i)
			if len(numbers) == 10:
				outputline = 'Case #' + str(case) + ': ' + str(N*x)
				# print outputline
				break
			x += 1
			z += 1
			# print z
		case += 1
		outputfile.write(outputline + '\n')

		





