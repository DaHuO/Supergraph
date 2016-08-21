def SOLVE(N):
	full = set([1, 2, 3 , 4 ,5, 6, 7, 8, 9, 0])
	digits = set([int(n) for n in str(N)])
	Done = False
	i = 2
	while not Done:
		new_digits = set([int(c) for c in str(N * i)])

		if N == 0:
			return 'INSOMNIA'
		digits = digits.union(new_digits)
		if digits == full:
			return N * i
			break
		i += 1	

def answer():
	source = open("A-large.in", 'r')
	output = open("large-output.txt", 'w')
	first_line = True
	case = 1
	for line in source:
		if first_line:
			first_line = False
		elif line =='\n':
			pass
		else:
			output.write("Case #{0}: {1}\n".format(case, SOLVE(int(line))))
			case += 1

answer()