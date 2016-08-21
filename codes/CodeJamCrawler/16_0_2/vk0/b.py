f = open('B-large.in', 'r')
g = open('B-large.out', 'w')

for lines in range(int(f.readline())):
	stack = f.readline()
	flips = 0
	binary_stack=[]
	bad_cakes = []
	for i in range(len(stack[0:-1])):
		if(stack[i] == '-'):
			binary_stack.append(0)
			bad_cakes.append(i)
		else:
			binary_stack.append(1)
	
	if(len(binary_stack) == 1):
		if(binary_stack[0] == 0):
			binary_stack[0] = 1
			flips = flips + 1
	else:
		while(sum(binary_stack) < len(binary_stack)):
			location1 = 0
			location2 = 0
			location  = 0
			#print(binary_stack)
			for i in range(len(binary_stack)):
				if(binary_stack[i] == 0):
					location1 = i
					break
			
			for i in range(location1+1, len(binary_stack)):
				location2 = i
				if(binary_stack[i] == 1):
					break
			#print('this is location 1 & 2 : ', location1, location2)
			
			if(location2 > location1):
				for i in range(location1, location2+1):
					binary_stack[i] = 1
				if(location1 == 0):
					flips = flips + 1
				else:
					flips = flips + 2				
			else:
				binary_stack[location1] = 1
				flips = flips + 2

	g.write("Case #"+str(lines+1)+": "+str(flips)+"\n")
g.close()