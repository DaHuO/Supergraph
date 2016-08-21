t=int(input())
k=1
op=""
while k<=t:
	stack=input()
	if stack[0]=='+':
		op ='-'
	else :
		op = '+'
	ans=0	
	while 1:
		count=0
		for j in stack:
			if j=='+':
				count +=1				
		if len(stack)==count :
			print(('Case #%d: %d')%(k,ans))	
			break
		m=0		
		stclist=list(stack)
		for i in stack:
			if i != op :
				stclist[m]=op
				stack=''.join(stclist)
			else:
				break
			m +=1	

		if op=='+' :
			op='-'
		else:
			op='+'	
		ans +=1	
	k +=1	