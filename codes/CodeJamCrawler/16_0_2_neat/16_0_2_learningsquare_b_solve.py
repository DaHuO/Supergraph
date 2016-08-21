from gcj import *
from b_revenge import solve_case

def solve(inputs):
	outputs = []
	for item in inputs[1:]:
		case = []
		for char in item:
			if char == '+':
				case.append(1)
			elif char == '-':
				case.append(-1)
		output = solve_case(case)
		outputs.append(output)

	return outputs

def solve_to_file(filename_in, filename_out):
	inputs = read_input(filename_in)
	outputs = solve(inputs)
	print outputs
	write_output(outputs, filename_out)