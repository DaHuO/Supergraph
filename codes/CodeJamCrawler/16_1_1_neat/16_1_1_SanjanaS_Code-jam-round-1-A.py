
inp_file = open('A-large.in', 'r').readlines()
out_file = open('Code_jam_round_1_A_large.out', 'w')

n_cases = int(inp_file[0].strip())
for i in range(1, n_cases+1):
	inp_str = list(inp_file[i].strip())
	output_str = [inp_str[0]]
	for char in inp_str[1:]:
		if(char >= output_str[0]):
			output_str.insert(0, char)
		else:
			output_str.append(char)

	out_file.write("Case #" + str(i) + ": " + ''.join(output_str) + "\n")