L=[]
for t in range(int(input())):
	n=int(input())
	l=[]
	prev='A'
	c=1
	t=n
	while(True):
		n=t*c
		c+=1
		for i in str(n):
			if i not in l:
				l.append(i)
		if prev==n:
			L.append('INSOMNIA')
			break
		if len(l)==10:
			L.append(str(n))
			break
		prev=n
c=1
s=""
for i in L:
	s+="Case #"+str(c)+":"+" "+i+"\n"
	c+=1
f=open('output','w')
f.write(s)
f.close()

