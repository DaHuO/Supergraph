import os

file_path_input = os.getcwd() + '/' + 'prob2.in'
file_path_output = os.getcwd() + '/' + 'prob2.out'

with open(file_path_output, 'wb') as output_data:
	with open(file_path_input, 'rb') as input_data:
			num_cases = int(input_data.readline())

			for i in range(num_cases):
				curr_stack = list(input_data.readline().decode())
				try:
					curr_stack.remove('\n')
				except: 
					nothing = 1

				if len(curr_stack) == 1:
					if curr_stack[0] == '-':
						out_line = 'Case #' + str(i+1) + ': 1\n' 
						output_data.write(out_line.encode())
					else:
						out_line = 'Case #' + str(i+1) + ': 0\n'
						output_data.write(out_line.encode())

				else:
					iter1 = 0
					iter2 = 1
					count = 0
					while '-' in curr_stack:
						if '+' not in curr_stack:
							count += 1
							break

						while curr_stack[iter1] == curr_stack[iter2]:
							if iter2 <= len(curr_stack)-2:
								iter1 += 1
								iter2 += 1

						if curr_stack[iter1] == '-':
							for j in range(iter2):
								curr_stack[j] = '+'
							count += 1
							prev = '+'
						else:
							for j in range(iter2):
								curr_stack[j] = '-'
							count += 1
							prev = '-'

					out_line = 'Case #' + str(i+1) + ': ' + str(count) + '\n'
					output_data.write(out_line.encode())

	input_data.close()
output_data.close()