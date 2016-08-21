filename = 'D-small-attempt0.in'
#filename = 'case.in'
with open(filename) as f:
	str_list = []
	case_num = f.readline().rstrip()
	str_list = [line.split() for line in f]
num_list = [[int(i) for i in j] for j in str_list]

output_file = 'output.txt'
output = open(output_file, 'w')

for i in range(int(case_num)):
	k = num_list[i][0]
	c = num_list[i][1]
	s = num_list[i][2]
	if s < k-c+1:
		output.write("Case #%s: IMPOSSIBLE\n" % (i+1))	
		continue
	
	output.write("Case #%s:" % (i+1))
	for i in range(1,k+1):
		num = k**(c-1)*i
		output.write(" %d" % num)
	output.write("\n")
