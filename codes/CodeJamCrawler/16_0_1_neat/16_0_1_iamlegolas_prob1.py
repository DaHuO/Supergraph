import os

file_path_input = os.getcwd() + '/' + 'prob1.in'
file_path_output = os.getcwd() + '/' + 'prob1.out'

with open(file_path_output, 'wb') as output_data:
	with open(file_path_input, 'rb') as input_data:
			num_cases = int(input_data.readline())

			for i in range(num_cases):
				check_arr = [0]*10
				
				curr_numStr = input_data.readline().decode()
				curr_numInt = int(curr_numStr)

				if curr_numInt == 0:
					out_line = 'Case #' + str(i+1) + ': INSOMNIA'
					output_data.write(out_line.encode())
					output_data.write('\n'.encode())

				else:
					mult = 2
					updated_numInt = curr_numInt
					while 0 in check_arr:
						curr_numStr = list(str(updated_numInt))

						for num in curr_numStr:
							check_arr[int(num)] = 1

						updated_numInt = curr_numInt * mult
						mult += 1

					updated_numInt -= curr_numInt
					out_line = 'Case #' + str(i+1) + ': ' + str(updated_numInt)
					output_data.write(out_line.encode())
					if i != num_cases-1:
						output_data.write('\n'.encode())