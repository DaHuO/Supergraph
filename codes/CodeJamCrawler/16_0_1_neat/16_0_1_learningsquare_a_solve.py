from gcj import *
from a_countingsheep import solve_case

def solve(inputs):
	outputs = []
	for item in inputs[1:]:
		case = int(item)
		output = solve_case(case)
		if output == -1:
			output = 'INSOMNIA'
		outputs.append(output)

	return outputs

def solve_to_file(filename_in, filename_out):
	inputs = read_input(filename_in)
	outputs = solve(inputs)
	print outputs
	write_output(outputs, filename_out)