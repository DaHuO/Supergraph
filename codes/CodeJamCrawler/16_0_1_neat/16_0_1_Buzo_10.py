import copy
test = int(raw_input())
a=0

while(a<test):
	a=a+1
	#input of intial no
	n = int(raw_input())
	b = []
	c=[]
	e=[]
	d=[0,1,2,3,4,5,6,7,8,9]
	f=[]
	i=1
	if n==0:
		print ("Case #%r: INSOMNIA"%a)
	else:
		while True:
			b.append(n*i)
			
			c = [int(j) for j in str(b[i-1])]
			
			
			e = [val for val in c if val in d]
			
			
			
			if i>1:
				e = list(set().union(e,f))
				
				
			f=e
			
			i=i+1
			
			
			if (len(e)==10):
				print "Case #%r: %r"%(a,n*(i-1))
				break
	
			