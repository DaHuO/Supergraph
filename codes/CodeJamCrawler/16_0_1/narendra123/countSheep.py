t=int(input())
k=1
while k<=t:
	d=dict()
	n=int(input())
	j=1
	num=n
	flag=0
	while 1:
		if n==0:
			print(('Case #%d: INSOMNIA')%k)
			break
		for e in str(num) :
			if e in d :
				d[e] +=1
				if len(d)>9 :
					print(('Case #%d: %d')%(k,num))
			else :
				d[e] =1	
				if len(d)>9 :
					print(('Case #%d: %d')%(k,num))
			if len(d)==10 :
				flag=1
				break;
		if flag==1:
			break;				
		j +=1 
		num =n*j
	k +=1	