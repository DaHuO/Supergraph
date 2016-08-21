i=open("d.in","r");
o=open("d.out","w");
t=int(i.readline())
for z in range(t):
	te=i.readline().split();print te;
	k=int(te[0]);c=int(te[1]);s=int(te[2]);
	d=[];
	for x in range(k):
		d.append(str(x+1));
	o.write("Case #"+str(z+1)+": "+' '.join(d)+"\n");
