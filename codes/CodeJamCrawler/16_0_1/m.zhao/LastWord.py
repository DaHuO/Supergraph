
read = open('in.in', 'r')
write = open('out.out', 'w')

cases = int(read.readline())

for case in range(cases):
	
	line = read.readline()[:-1]

	string = ""

	for i in range(len(line)):
		if string == "" or line[i] >= string[0]:
			string = line[i] + string
		else:
			string = string + line[i]


	
	write.write("Case #{0}: {1}\n".format(case+1, string))

read.close()
write.close()


