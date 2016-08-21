from gcj import *
from a_lastword import solve_case

def solve(inputs):
	outputs = []
	for item in inputs[1:]:
		case = item.rstrip()
		output = solve_case(case)
		outputs.append(output)

	return outputs

def solve_to_file(filename_in, filename_out):
	inputs = read_input(filename_in)
	outputs = solve(inputs)
	print outputs
	write_output(outputs, filename_out)