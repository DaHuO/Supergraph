import sys

input_list = []
output_list = []

try:
	input_filename = sys.argv[1]
	output_filename = input_filename[:sys.argv[1].find('.')]+'.out'
except:
	print 'input filename as argv'
	exit()

def get_last_num(N):
	if N == 0:
		return -1
	include_arr = [0,0,0,0,0,0,0,0,0,0]
	for i in range(1, 100000):
		str_iN = str(i*N)
		for j in range(len(str_iN)):
			int_str_iNj = int(str_iN[j])
			if include_arr[int_str_iNj] == 0:
				include_arr[int_str_iNj] = 1
			else:
				pass
		if 0 in include_arr:
			pass
		else:
			return str_iN
	return -1

try:
	input_f = open("./"+input_filename)
	input_lines = input_f.readlines()
	input_count = 0
	for input_line in input_lines:
		# input_split = input_line.split()
		input_list.append(int(input_line))
	input_f.close()
except:
	print 'read error'
	exit()

input_list.pop(0)

for input_item in input_list:

	# do some works here
	
	result = get_last_num(input_item)
	# result += ''
	if result == -1 :
		output_list.append(['INSOMNIA'])
	else:
		output_list.append([result])

try:
	output_f = open("./"+output_filename, "w")
	output_f.close()
except:
	pass

try:
	output_f = open("./"+output_filename, "a")
	output_str = ''

	for x in range(len(output_list)):
		output_f.write('Case #' + str(x+1)+': '+str(output_list[x][0])+"\n")
		print x
	output_f.close()
except:
	print 'write error'
	exit()
