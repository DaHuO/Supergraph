def flip(s,n):
	s=list(s)
	k=[]
	for i in range(n):
		if(s[i]=='+'):
			k.append('-')
		else:
			k.append('+')
	s=k[::-1]+s[n:]
	return ''.join(s)
for t in range(int(raw_input())):
	s=raw_input()
	count=0
	for i in range(len(s)-1):
		if(s[i]!=s[i+1]):
			s=flip(s,i+1)
			count+=1
	if(s[0]=='-'):
		count+=1

	print("Case #"+str(t+1)+": "+str(count)	)