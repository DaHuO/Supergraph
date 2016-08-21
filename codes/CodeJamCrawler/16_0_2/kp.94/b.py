def flip(a,i):
	for j in xrange(i/2 +1):
		if a[j]==a[i-j] and j!=i-j:
			a[j]=(a[j]+1)%2
			a[i-j]=(a[i-j]+1)%2
		if j==i-j:
			a[j]=(a[j]+1)%2
	
	return a

	
t=input()
for _ in xrange(t):
	a=list(raw_input())
	n=len(a)
	for i in xrange(n):
		if a[i]=="+":a[i]=1
		else: a[i]=0
	if 0 not in a:
		print("Case #{}: {}".format(_+1,0))
	else:
		flips=0
		#i=n-1
		while True:
			if 0 not in a:flips-=1;break
			if 1 not in a:break
			if (n-1-a[::-1].index(0))+1== a.index(1):break
			f=0
			#if i<0:i=n-1
			for i in xrange(n-1,-1,-1):
				if a[0]==a[i] and i!=0:
					if a[0]==1 and (0 not in a[0:i+1]):
						a=flip(a,i)
						flips+=1
						f=1	
						break
					
					elif a[0]==0 and (1 in a[0:i+1]):
						a=flip(a,i)
						flips+=1
						f=1
				
					
			if f==0:
				a[0]=(a[0]+1)%2
				flips+=1
			
			
		print("Case #{}: {}".format(_+1,flips+1))
