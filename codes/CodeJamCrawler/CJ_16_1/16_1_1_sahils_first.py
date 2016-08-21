f=open("A-large.in")
o = open("ofirst.txt", 'w')
T= f.readline()
c=0
for c in range(int(T)):
	n=f.readline().strip()
	n=list(n)
	s=n[0]
	for i in range(len(n)-1):
		if(n[i+1]>=s[0]):
			s=n[i+1]+s
		else:
			s=s+n[i+1]
	o.write("Case #"+str(c+1)+": "+s)
	o.write('\n')
	