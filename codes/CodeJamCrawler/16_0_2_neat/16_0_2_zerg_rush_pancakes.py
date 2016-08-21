with open("B-large.in") as infile, open("OutputPancakes.txt", 'w') as outfile:
	first = True
	case = 1
	for line in infile:
		if first:
			ntests = int(line)
			first = False
		else:
			print line
			test_input = line
			list_input = [1 if i == '+' else 0 for i in list(test_input.strip())]
			# print list_input
			target = list_input[0]
			moves = 0
			n = len(list_input)
			while sum(list_input) != n:
				moves += 1
				for i in range(n):
					if list_input[i] == target:
						list_input[i] = 0 if list_input[i] == 1 else 1
					else:
						break
				target = 1 if target == 0 else 0
			outfile.write('Case #{}: {}\n'.format(case, moves))
			case += 1
