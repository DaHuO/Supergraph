# your code goes here
for t in range(1,int(input())+1):
	n=int(input())
	l=[]
	for i in range(10):
		l.append(0)
	c=0
	if(n==0):
		print("{0}{1}{2}{3}".format('Case #',t,': ','INSOMNIA'))
	else:
		i=n
		while True:
			if c==10:
				break
			j=i
			while j!=0:
				a=j%10
				if c==10:
					break
				if l[a]==0:
					c+=1
					l[a]=1
				j=j//10
			if c==10:
				break
			i+=n
		print("{0}{1}{2}{3}".format('Case #',t,': ',i))