c={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
def count(n):
	while n!=0:
		d=n%10
		c[d]+=1
		n/=10
	return

t=int(raw_input())
for i in xrange(t):
	n=int(raw_input())
	if n==0:
		print ("Case #"+str((i+1))+": INSOMNIA")
	else:
		j=1
		awake=True
		while awake:
			temp=0
			count(j*n)
			for k in c:
				if(c[k]==0):
					temp+=1
			if(temp==0):			
				for k in c:
					c[k]=0
				print ("Case #"+str((i+1))+": "+str(j*n))
				awake=False
			else:
				j+=1