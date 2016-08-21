myset = set('')
file = open('A-large.in','r')
ofile = open('output.txt','w')

total = 0
total = int(file.readline())

for i in range(total):
	done = False
	N = int(file.readline())

	ofile.write("Case #"+str(i+1)+": ")

	for i in range(10000000):
		if i==0:
			continue
		instr = str(N*i)
		# print instr
		for char in instr:
			myset.add(char)
			if (('0' in myset) and ('1' in myset) and ('2' in myset) and ('3' in myset) and ('4' in myset) and ('5' in myset) and ('6' in myset) and ('7' in myset) and ('8' in myset) and ('9' in myset)):
				ofile.write(instr)
				myset.clear()
				done = True
				break
		if done:
			break
	if not done:
		ofile.write("INSOMNIA")
	ofile.write("\n")
	myset.clear()