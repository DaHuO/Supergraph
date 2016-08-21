import os

def get_input():
	with open('input.txt') as input_file:
	    testCases = input_file.readlines()
	return testCases

def prep_output():
	output_filename = 'output.txt'
	if os.path.exists(output_filename):
		os.remove(output_filename)

def write_output(index, string):
	output_filename = 'output.txt'
	with open(output_filename, 'a') as output_file:
		output_file.write('Case #' + str(index+1) + ': ' + str(string) + '\n')
