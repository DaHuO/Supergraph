def maneuver(n1):
	stack=[]
	global s
	temp=list(s)
	k=0
	while k<=n1:
		if(temp[k]=='-'):
			stack.append('+')
		else:
			stack.append('-')
		k+=1  
	k=n1
	while k>=0:
		temp[k]=stack.pop()	
		k-=1
	s="".join(temp)
	#print s
	return 

t=int(raw_input())
for i in xrange(t):
	flips=0
	s=raw_input()
	n=len(s)
	complete=False
	while  not complete:
		j=n-1
		while(j>=0 and s[j]!='-'):
			j-=1

		#print str(j)
		if (j==-1 and s[j]=='+'):
			complete=True
			print ("Case #"+str((i+1))+": "+str(flips))
			break
		if(j!=(n-1)):
			n=j
		j=0
		#print str(n)
		while(j<n and s[j]!='-'):
			j+=1
		if j!=0:
			maneuver(j-1)
			flips+=1
		maneuver(n-1)
		flips+=1
