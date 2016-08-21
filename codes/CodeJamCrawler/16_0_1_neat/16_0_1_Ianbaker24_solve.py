import sys

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	line = in_file.readline().replace('\n', '')
	n = int(line)
	
	if(n == 0):
		out_file.write('INSOMNIA')
	else:
		numbers_left = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		iterations = 1
		while(len(numbers_left) > 0):
			number = iterations * n
			while(number > 0 and len(numbers_left) > 0):
				digit = number % 10
				number /= 10
				if(numbers_left.count(digit) > 0):
					numbers_left.pop(numbers_left.index(digit))
			iterations += 1
		
		out_file.write(str((iterations - 1) * n))
	
	out_file.write('\n')

if len(sys.argv) != 2:
	print 'Please provide one parameter with the name of the input file location relative to this file.'
else:
	in_file = open(str(sys.argv[1]), 'r')
	out_file = open(str(sys.argv[1]).replace('.in', '.out'), 'w')
	cases = int(in_file.readline())
	case = 0
	while (case < cases):
		solve(in_file, out_file, case)
		case += 1
	in_file.close()
	out_file.close()