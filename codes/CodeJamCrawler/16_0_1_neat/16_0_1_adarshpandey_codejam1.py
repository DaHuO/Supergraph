import string
data=open("A-large.in","r")
s1=data.read()
s1=s1.split("\n")
t=int(s1[0])
for i in range(1,t+1):
	n=int(s1[i])
	if(n==0):
		print("Case #{0}: INSOMNIA".format(i))
		continue
	s=str(n)
	c=0
	l=[0 for j in range(10)]
	m=1
	while (True):
		s=str(n*m)
		for j in s:
			k = int(j)
			if(l[k]==0):
				l[k]=1
				c+=1
			if(c==10):
				break
		if(c==10):
			break
		else:
			m+=1
	if(c==10):
		print("Case #{0}: {1}".format(i,n*m))


