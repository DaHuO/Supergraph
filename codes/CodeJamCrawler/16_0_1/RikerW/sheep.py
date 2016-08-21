import itertools
stack = []
infile = open("A-small-attempt4.in",'r').read()
outputfile = open('output.out', 'w')
counter = 0
for current_num in infile.split('\n')[1:]:
	counter += 1
	if current_num == '':
		continue
	current_num = int(current_num)
	for i in itertools.count(current_num,current_num):
		print current_num
		stack = list(set(stack + list(str(i))))
		print stack
		if set(stack) == set([str(j) for j in range(0,10)]):
			outputfile.write("Case #" + str(counter) + ": " + str(i)+'\n')
			break
	
		if i >= current_num**current_num and i >= current_num*200:
			outputfile.write("Case #" + str(counter) + ": INSOMNIA\n")
			break
		if current_num == 0:
			outputfile.write("Case #" + str(counter) + ": INSOMNIA\n")
			break
		
	stack = []
