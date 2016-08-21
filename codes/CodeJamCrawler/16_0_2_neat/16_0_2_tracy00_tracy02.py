t = raw_input()
t=int(t)
count=0
for i in range(0,t):
	count=count+1
	
	result=0
	
	stream = raw_input()
	p=0
	
	
	height = len(stream)
	
	if(stream[p]=='-'):
		while(p< height and stream[p]!='+'):
			p=p+1
		result=result+1
	
	while((p+1)<height):
		if(stream[p]=='+' and stream[p+1]=='-'):
			result=result+2
		p=p+1
		
				
	print("Case #"+str(count)+": "+str(result))
