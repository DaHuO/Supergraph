f=open('/Users/sb17/Downloads/A-large.in')
data=f.readlines()

f_t=open('/Users/sb17/Downloads/output.out','w')
t=int(data[0])

k=1

while(t>0):
	
	a=int(data[k])
	
	l=[0,0,0,0,0,0,0,0,0,0]
	if(a==0):
		string="INSOMNIA"
		
		f_t.write("Case #%d: %s" %(k,string))
		f_t.write('\n')		

		
	else:	
		inp=a
		j=1
	
		while(sum(l)!=10):
			b=str(inp)
		
			for i in range(len(b)):
				c=b[i]
				
				ch=int(c)
		
				if l[ch]!=1:
					l[ch]=1
			if(sum(l)==10):
				num=int(b)
				
				
				f_t.write("Case #%d: %d" %(k,num))
				f_t.write('\n')
			
			else:
				j+=1
				inp=a*j
	k+=1
	t=t-1
f_t.close()