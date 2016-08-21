import traceback

def remove_nums(num, check_list):
	for elm in str(num):
		f_num =  int(elm)
		if f_num in check_list:
			check_list.remove(f_num)
	return check_list

def check_sequence_exists(num):
	check_list = [0,1,2,3,4,5,6,7,8,9]
	data_list = remove_nums(num,check_list)
	sequence = 1
	mul = 0
	while data_list != []:
		mul = num * sequence
		data_list = remove_nums(mul,data_list)
		sequence += 1
	return mul
def get_results(content):
	total_cases = int(content[0].rstrip())
	file_write = open("output.txt", "wb")
	for i in range(1,total_cases+1):
		num = int(content[i].rstrip())
		if  num == 0:

			file_write.write( "Case #1: INSOMNIA\n" )
		else:
			data =  "Case #" + str(i)+": " +str((check_sequence_exists(num))) + str("\n")
			file_write.write( str(data))


with open("A-large.in") as f:
	try:
	    content = f.readlines()
	    get_results(content)
	except:
		traceback.print_exc()
