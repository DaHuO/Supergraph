N=[]
T=int(input())
answer=0
for i in range(T):
	temp=raw_input()
	N.append(temp)
for o,j in enumerate(N):
	answer=0
	stack=list(j)
	while('-' in stack):
		same=stack[0]
		switch=0
		for i in stack:
			if(i!=same):
				answer+=1
				for ite in range(switch):
					if(stack[ite]=='+'):
						stack[ite]='-'
					else:
						stack[ite]='+'
				break
			else:
				switch+=1
		if(switch==len(stack)):
			answer+=1
			for il in range(len(stack)):
					stack[il]='+'
	print("Case #"+str(o+1)+": "+str(answer))