def pancakes(a,count):
	if a==[''] or a==[]:
		quit()
		
	c=True
	for k in a:
		if k=='-':
			c=False
	
	if c==True:
		return(count)
	else:
		a.reverse()
		for i in range(len(a)):
			if a[i]=='-':
				break
		a.reverse()
		for j in range(len(a)-i):
			if a[j]=='+':
				a[j]='-'
			elif a[j]=='-':
				a[j]='+'
		count=count+1
		return pancakes(a,count)
		



f=open('B-large.in','r')
g=open('codejam2.txt','w')

x='sheep'
count2=1
simple=f.readline()

while x!='':
	y=f.readline()
	q=''
	count=0
	for s in range(len(y)-1):
		q=q+y[s]
		
	y=q	
	a=list(y)
	ans=pancakes(a,count)
	ans2='Case #{0}: {1}'.format(count2,ans)
	g.write(ans2)
	g.write('\n')
	x=y
	count2+=1
	

f.close()
g.close()
