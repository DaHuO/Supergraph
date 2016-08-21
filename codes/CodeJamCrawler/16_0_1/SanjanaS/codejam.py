input_lines = open('A-large.in', 'r').readlines()
output_file = open('A-large-output.out', 'w')
n_inputs = input_lines[0]
for line in input_lines[1:]:
	num = int(line.strip())
	if(num == 0):
		output_file.write("Case #" + str(input_lines.index(line)) + ": INSOMNIA" + "\n")
		continue
	orig_num = int(line.strip())
	count = 1
	digits = set()
	while(len(digits) < 10):
		num = orig_num * count
		count += 1
		digits.update(list(str(num)))

	output_file.write("Case #" + str(input_lines.index(line)) + ": " + str(num) + "\n")



