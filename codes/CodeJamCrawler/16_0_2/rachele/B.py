input_file = "B-large.in"
output_file = "Blarge.out"

f_in = open(input_file, "r")
f_out = open(output_file, "w")

test_cases = int(f_in.readline()[:-1])

for case in range(test_cases):
	f_out.write("Case #" + str(case+1) + ": ")
	p = f_in.readline()
	res = 0
	if p[-1]=="\n":
		p = p[:-1]
	blocks = 1
	for i in range(1,len(p)):
		if p[i-1] != p[i]:
			blocks +=1
	plus_end = False
	if p[-1] == '+':
		plus_end = True
	if plus_end:
		res = blocks -1
	else:
		res = blocks
	f_out.write(str(res)+"\n")


f_in.close()
f_out.close()