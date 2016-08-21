t=int(input())
for i in xrange(1,t+1) :
	n=int(input())
	if n==0 :
		print ("Case #%d: INSOMNIA")%(i);
	else :
		num=n
		dgts=set()
		while len(dgts)!=10 :
			dummy=num
			while dummy :
				dgts.add(dummy%10)
				dummy/=10
			num+=n
		print ("Case #%d: %d")%(i,num-n);
	
			
	
