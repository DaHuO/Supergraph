

def get_total_count(input_num):
	if input_num == 0:
		return "INSOMNIA"
	num_set = set()
	target_num = input_num
	loop_count = 1
	while(True):
		insert_each_number(num_set, target_num)
		if len(num_set) == 10:
			break
		loop_count += 1	
		target_num = input_num * loop_count
	return target_num 
	

def insert_each_number(num_set, target_num):
	for c in str(target_num):
		num_set.add(c)


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	input_num = int(input())
	print("Case #{}: {}".format(i, get_total_count(input_num)))
