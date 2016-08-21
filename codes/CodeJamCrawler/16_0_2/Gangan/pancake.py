cases = int(input())

def flip(substack):
	substack = substack[::-1]
	substack=substack.replace("+","0")
	substack=substack.replace("-","+")
	substack=substack.replace("0","-")
	return substack

for case in range(cases):
	stack = input()
	i=0
	while(stack.find("-")!=-1):
		i+=1
		if(stack.find("+")==-1):
			break
		n = stack.find("-" if stack[0]=="+" else "+")
		stack = flip(stack[0:n])+stack[n::]
	print("Case #"+str(case+1)+": "+str(i))