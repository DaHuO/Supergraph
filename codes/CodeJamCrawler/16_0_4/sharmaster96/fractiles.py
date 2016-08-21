def epilogue(result, num):
	out_file.write("Case #" + str(num+1) + ": " + result + '\n')

in_file, out_file = open('D-small-attempt0.in', 'r'), open('D-small-attempt0.out', 'w')

num_cases = int(in_file.readline())
for case_num in range(num_cases):
	K, C, S = [int(i) for i in in_file.readline().split()]
	addend, upper_limit = K**(C-1), K**C
	i = 1
	positions = []
	while i <= upper_limit:
		positions.append(i)
		i = i + addend
	epilogue(" ".join([str(i) for i in positions]), case_num)