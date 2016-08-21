h=open("A-large.in")
o=open("output.txt","a")
f=h.readlines()
t =int(f[0])
x=[]
y=[]
for a in xrange(1,t+1):
	s=f[a]
	st=list(s)
	elem=st[0]
	l=len(st)
	for i in xrange(1,l):
		x.append(elem)
		m=len(elem)
		x.append(st[i])
		x.sort(reverse=True)
		if m>=2 and elem==x[0]:
			del y[:]
			y=list(x[0])
			if y[0]==x[1]:
				temp=x[1]
				x[1]=x[0]
				x[0]=temp
		elem=''.join(x)
		del x[:]
	o.write("Case #"+str(a)+": "+elem)

