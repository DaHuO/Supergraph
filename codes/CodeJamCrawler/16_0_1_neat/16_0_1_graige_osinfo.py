
fp = open("A-large.in","r")
fpa = open("A-small-attempt5.out","w")

t=int(fp.readline())
a=[]
c=1
p=0
while t:
	p+=1
	t-=1
	d=int(fp.readline())
	c=1
	if d==0:
		#print "INSOMNIA"
		fpa.write("Case #"+str(p)+": INSOMNIA\n")

	else:
		a=[0 for i in range(10)]
		while True:
			w=c*d
			while w>0:
				a[w%10]+=1;
				w/=10
			c+=1
			w=0
			for i in a:
				if i!=0:
					w+=1;
			if w==10:
				break;
		if c>=1000000:
			print "INSOMNIA"
			fpa.write("Case #"+str(p)+": INSOMNIA\n")
			c=-1
		if c!=-1:
			c-=1
			print c*d
			fpa.write("Case #"+str(p)+": "+str(c*d)+"\n")
fp.close()
fpa.close()