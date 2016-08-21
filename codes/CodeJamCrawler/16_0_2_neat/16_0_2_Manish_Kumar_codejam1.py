h=open("try.in")
o=open("output.txt","a+")
f=h.readlines()
t =int(f[0])
r=0
for a in range(1,t+1):
	r=r+1
	p=f[a].split()
	p=[c for c in p[0]]
	i=0
	count=0
	c=0
	for x in p:
			if x=='+':
				c=c+1
	if c==len(p):
		o.write("Case #"+str(r)+": "+str(count)+"\n")
	elif len(p)==1:
		if p[0]=='-':
			count=1
			o.write("Case #"+str(r)+": "+str(count)+"\n")
	else:
		c=0
		while c!=len(p):
			c=0
			i=1
			while i<len(p) and p[0]==p[0+i]:
				i=i+1
			if p[0] == '+':
				for a in range(0,i):
					p[a]='-'
				count=count+1
			else:
				for a in range(0,i):
					p[a]='+'
				count=count+1
			for x in p:
				if x=='+':
					c=c+1
		o.write("Case #"+str(r)+": "+str(count)+"\n")