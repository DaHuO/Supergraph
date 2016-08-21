def get_upper(num):
	if num == 0:
		return None
	nums = [0,1,2,3,4,5,6,7,8,9]
	new_num = num
	while (nums):
		temp = new_num
		while (temp):
			digit = temp%10
			if digit in nums:
				nums.remove(digit)
			temp /= 10
		new_num += num
	return new_num-num 

#case_num = raw_input()
filename = 'A-large.in'
with open(filename) as f:
	num_list = []
	case_num = f.readline().rstrip()
	for line in f:
		ele = int(line.strip())
		num_list.append(ele)

output_file = 'output_large.txt'
output = open(output_file, 'w')

for i in range(int(case_num)):
	#num = raw_input()
	num = num_list[i]
	upper_num = get_upper(int(num))
	if upper_num == None:
		upper_num = "INSOMNIA"
	print ("Case #%s: %s" % (i+1, upper_num))
	output.write("Case #%s: %s\n" % (i+1, upper_num))
