t=input()
c=1
while t>0:
	n=input()
	if(n==0):
		print "Case #"+str(c)+": INSOMNIA"
	else:
		d=[0]*10
		oZ=ord('0')
		m=0
		while(sum(d)<10):
			m+=n
			s=str(m)
			for i in s:
				d[ord(i)-oZ]=1;
		print "Case #"+str(c)+": "+str(m)
	c+=1
	t-=1
