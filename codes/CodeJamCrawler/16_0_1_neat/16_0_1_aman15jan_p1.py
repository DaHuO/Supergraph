t=int(input())
for i in range(t):
	n=int(input())
	dict={}
	p=0
	a=0
	c=1
	q=n
	if(n==0):
		print("{0}{1}{2}{3}".format('Case #',i+1,': ','INSOMNIA'))
		continue
	else:
		while(True):
			b=q
			while(b!=0):
				temp=b%10
				if temp not in dict.keys():
					dict[temp]=''
					p+=1
					if(p==10):
						print("{0}{1}{2}{3}".format('Case #',i+1,': ',q))
						a=1
						break
				b=b//10
			if(a==1):
				break
			else:
				c+=1
				q=n*c
						
				
	
			
