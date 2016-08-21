
for i in range(input()):
	a=list()
	t=list(str(raw_input()))
	k=ord(t[0])
	for j in range( len(t)):
		if(ord(t[j])>=k):
			k=ord(t[j])
			a.insert(0,t[j])
		else:
			a.append(t[j])
			
	print"Case #%d: %s"%(i+1,''.join(a))
			
	

			
			
			
			
	