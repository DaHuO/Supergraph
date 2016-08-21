from gcj import *
from c_coinjam import solve_case

def solve(inputs):
	outputs = []
	for item in inputs[1:]:
		case = [int(i) for i in item.split()]
		jamcoins, divisorlists = solve_case(case[0], case[1])

		output = ''

		for i in range(len(jamcoins)):
			subcase_output = str(jamcoins[i])
			for divisor in divisorlists[i]:
				subcase_output += ' ' + str(divisor)

			output += '\n' + subcase_output

		outputs.append(output)

	return outputs

def solve_to_file(filename_in, filename_out):
	inputs = read_input(filename_in)
	outputs = solve(inputs)
	print outputs
	write_output(outputs, filename_out)