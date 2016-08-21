def str_process(raw_str):
	i = 1
	while i < len(raw_str):
		if raw_str[i-1] == raw_str[i]:
			raw_str = raw_str[:i-1]+raw_str[i:]
		else: i += 1
	if raw_str[len(raw_str)-1] == '+':
		raw_str = raw_str[:len(raw_str)-1]
	return raw_str

filename = 'B-large.in'
with open(filename) as f:
	str_list = []
	case_num = f.readline().rstrip()
	for line in f:
		ele = line.strip()
		str_list.append(ele)

output_file = 'output_large.txt'
output = open(output_file, 'w')

for i in range(int(case_num)):
	raw_str = str_list[i]
	new_str = str_process(raw_str)
	
	output.write("Case #%s: %s\n" % (i+1, len(new_str)))
