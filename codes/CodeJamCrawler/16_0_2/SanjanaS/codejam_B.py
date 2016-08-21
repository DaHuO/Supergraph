input_lines = open('B-large.in', 'r').readlines()
output_file = open('B-out-large.out', 'w')

n_inputs = int(input_lines[0])

for i in range(1, n_inputs + 1):
	in_str = input_lines[i].strip()
	n_moves = 0
	plus_flag = False
	ind = 0
	
	in_str = list(in_str)

	while('-' in in_str):
		if(ind == 0 and in_str[ind] == '-'):
			while(ind < len(in_str) and in_str[ind] != '+'):
				in_str[ind] = '+'
				ind += 1
			n_moves += 1
			ind = 0
		elif(ind == 0 and in_str[ind] == '+' and ind < len(in_str)):
			while(ind < len(in_str) and in_str[ind] != '-'):
				in_str[ind] = '-'
				ind += 1
			n_moves += 1
			ind = 0

	output_file.write("Case #" + str(i) + ": " + str(n_moves) + "\n")