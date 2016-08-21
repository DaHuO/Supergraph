def flip(x,a,b):
	for i in range(a,b+1):
		if(x[i]=='-'):
			x[i]='+'
		else:
			x[i]='-'
	return x

n=input()
for i in range(n):
	print "Case #%s:"%(i+1),
	x=raw_input()
	x=list(x)
	l=len(x)
	pos=1
	ans=0
	for j in range(l):
		if(x[l-j-1]=='+'):
			continue
		else:
			x=flip(x,0,l-j-1)
			ans+=1
	print ans
