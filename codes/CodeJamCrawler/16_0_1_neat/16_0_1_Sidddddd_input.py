def sleep(_,n):
	if n==0:
		print "Case #%d: INSOMNIA"%(_+1)
		return
	else:
		nos=['0','1','2','3','4','5','6','7','8','9']
		found=sorted(list(str(n)))
		i=2
		while bool(sorted(set(found))!=nos): 
			found.extend(sorted(list(str(n*i))))
			i+=1
		print "Case #%d: %d"%(_+1,(i-1)*n)
cases=int(input())
for _ in xrange(cases):
	n=input()
	sleep(_,n)


	
			

	
	


	
	
			
	 

			
		

	
					