file = open("B-large.in", 'r')
fileW = open("answer", 'w')
countTests = int(file.readline())
for currentTest in range(countTests):
	count = 0
	stack = list(file.readline())
	if stack[len(stack)-1] == '\n':
		stack.remove('\n')
	flag = stack[0]
	toChange = False
	for i in stack:
		if i != flag :
			if i == '-':
				count += 0
			flag = i
			count += 1
			toChange = True
	
	if (not toChange)and flag == '-':
		count+=1
	else:
		if stack[len(stack)-1] == '-':
			count += 1

	fileW.write("Case #{}: {}\n".format(currentTest+1,count))
