for x_ in xrange(int(raw_input())):
	astr = list(raw_input())
	cnt = 0
	while ('-' in astr):
		stack = []
		pos = 0
		flag = True
		for y in astr:
			if y == '+' and flag:
				stack.append('-')
			else:
				flag = False
		#print astr,stack
		j = len(stack) - 1
		if j >=0:cnt+= 1
		for i in stack:
			astr[j] = i
			j -= 1
		#print'->', astr
		stack = []
		for y in range(len(astr)):
			if '-' in astr[y:]:
				if astr[y] == '-':
					stack.append('+')
				else:stack.append('-')
		j = len(stack) -1
		if j >=0:cnt+= 1
		#print astr,stack
		for i in stack:
			astr[j] = i
			j -= 1
		#print'->', astr
	
	#print astr
	print 'Case #'+str(x_+1)+':',cnt