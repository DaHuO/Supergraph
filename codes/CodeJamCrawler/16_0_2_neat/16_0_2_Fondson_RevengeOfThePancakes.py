t = int(input())
for i in range(1, t + 1):
	stack=list(input())
	done=False
	count=0
	while not done:
		for j in range(len(stack)):
			if j+1<len(stack) and stack[j]!=stack[j+1]:
				count+=1
				toJoin=[]
				for k in reversed(range(j+1)):
					if stack[k]=='-':
						toJoin.append('+')
					else:
						toJoin.append('-')
					stack.pop(k)
				stack=toJoin+stack
				break;
			if len(stack)-1==j:
				if stack[len(stack)-1]=='+':
					done=True
				elif len(stack)-1==j and stack[len(stack)-1]=='-':
					count+=1
					done=True
	print ("Case #{}: {}".format(i, count))

	
