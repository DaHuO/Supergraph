for i in range(input()):
	b=set()
	t=input()
	k=t
	for j in range(1,1000000):
		for char in str(k):
			b.add(char)
		if(t==0):	
			print "Case #%d: INSOMNIA"%(i+1)
			break
		if(len(b)==10):
			print "Case #%d: %d"%(i+1,k)
			break
		else:
			k=t*j
		if(t>10000000):
			print "Case #%d: INSOMNIA"%k
			break