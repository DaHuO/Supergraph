t=input()
for _ in xrange(t):
	n=input()
	if n==0:y="INSOMNIA"
	else:
		d={}
		for i in xrange(10):d[i]=0
		tr=True
		a=n
		while tr:
			r=a
			while r!=0:
				d[r%10]+=1
				r/=10
			for i in xrange(10):
				if d[i]==0:tr=True;break
				else:tr=False
			a+=n
		y=a-n
	print("Case #{}: {}".format(_+1,y))
