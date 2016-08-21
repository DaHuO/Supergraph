def comp(char):
	cmpl=''
	if char=='+':
		cmpl='-'
	else:
		cmpl='+'
	return cmpl

def revcomp(string,end):
	out=""
	for i in range(end-1,-1,-1):
		out+=comp(str(list(string)[i]))
	out+=string[end:len(string)]
	return out

t=int(raw_input())
for i in range(t):
	stack=raw_input()
	happy=0
	count=0
	while happy<len(stack) and str(list(stack)[len(stack)-happy-1])=='+':
		happy+=1
	while happy<len(stack):
		starts_with=str(list(stack)[0])
		if starts_with=='+':
			tmp=happy
			while tmp<len(stack) and str(list(stack)[len(stack)-tmp-1])=='-':
				tmp+=1
			stack=revcomp(stack,len(stack)-tmp)
			count+=1
			starts_with=str(list(stack)[0])	
		stack=revcomp(stack,len(stack)-happy)
		count+=1	
		while happy<len(stack) and str(list(stack)[len(stack)-happy-1])=='+':
			happy+=1
	print "Case #"+str(i+1)+": "+str(count)
