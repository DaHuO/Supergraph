data=open("A-large0.in","r")
s1=data.read()
s1=s1.split("\n")
t=int(s1[0])
for i in range(1,t+1):
	n=int(s1[i*2-1])
	s=s1[i*2]
	l=list(map(int,s.split()))
	m=sum(l)
	s=""
	while(m>0):
		if(m==2):
			for j in range(n):
				if(l[j]!=0):
					s+=(chr(65+j)*l[j])
			m-=2
		elif(m==3):
			ind=l.index(max(l))
			s+=(chr(65+ind)+" ")
			l[ind]-=1
			m-=1
		else:
			p=max(l)
			c=0
			for j in range(n):
				if(l[j]==p):
					s+=chr(65+j)
					l[j]-=1
					m-=1
					c+=1
				if(c==2):
					break
			s+=" "
	print("Case #{0}: ".format(i)+s)