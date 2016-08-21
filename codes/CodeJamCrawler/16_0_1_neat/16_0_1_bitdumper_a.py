a=[0,0,0,0,0,0,0,0,0,0];
b=[];
i=open("a.in","r");
o=open("a.out","w");
t=int(i.readline());
def wrk(w):
	n=int(i.readline());
	c=0;g=0;
	while c==0:
		n1=(g+1)*n;g=g+1;
		if g>100:
			c=1;
		n2=list(str(n1));
		for h in range(len(n2)):
			if a[int(n2[h])]==0:
				a[int(n2[h])]+=1;
				b.append(1);
		if len(b)>=10:
			o.write("Case #"+str(w)+": "+str(n1)+"\n");
			c=1;
	if len(b)<10:
		o.write("Case #"+str(w)+": INSOMNIA\n");print len(b);

for f in range(t):
	wrk(f+1);
	b=[];a=[0,0,0,0,0,0,0,0,0,0];
