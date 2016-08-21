from __future__ import print_function
fo=open("input.txt","r")
fo2=open("output.txt","w")
t=int(fo.readline())
y=1
while(y!=t+1):
	i=1
	l=[]
	c=0
	n=int(fo.readline())
	while True:
		r=i*n
		l=l+[int(x) for x in list(str(r))]
		l=sorted(set(l))
		#print l
		#time.sleep(2)
		count=len(l)
		if(r==((i-1)*n)):
			c=c+1
			if(c==5):
				fo2.write("Case #%d: "%y)
				fo2.write ("INSOMNIA\n")
				break
		elif(count==10):
			fo2.write ("Case #%d: "%y)
			fo2.write ("%d\n"%r)
			break
		i=i+1
	y=y+1
