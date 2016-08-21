n = int(raw_input())
abc=0
for i in range(n):
	abc+=1
	stri = raw_input()
	ans=0
	length = len(stri)
	j=0
	if(stri[j]=='-'):
		while(j< length and stri[j]!='+'):
			j+=1
		ans+=1
	while((j+1)<length):
		if(stri[j]=='+' and stri[j+1]=='-'):
			ans+=2
		j+=1
		
				
	print("Case #"+str(abc)+": "+str(ans))
