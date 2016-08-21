def read_input(filename_in):
	f = open(filename_in, 'r')

	return f.readlines()

def write_output(outputs, filename_out):
	f = open(filename_out, 'w')

	for i in range(len(outputs)):
		f.write('Case #' + str(i+1) + ': ' + str(outputs[i]) + '\n')

	f.close()