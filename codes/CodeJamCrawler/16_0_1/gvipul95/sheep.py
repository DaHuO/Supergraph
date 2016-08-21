test=input()
w=test
while test != 0:
	i=0
	n=input()
	arr=[]	
	temp=n
	while True:
		if(arr==[0,1,2,3,4,5,6,7,8,9]):
			print "Case #"+str(w-test + 1)+":",temp-n
			break
		else:
			
			arr+=(map(int,str(temp)))	
			arr=list(set(arr))
			temp=temp+n
			arr.sort()
			i+=1
			if(temp==temp+n):
				print "Case #"+str(w-test + 1)+": INSOMNIA"
				break	
				
	test-=1
