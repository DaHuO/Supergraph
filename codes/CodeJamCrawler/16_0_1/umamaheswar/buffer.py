import sys
t=int(input())
for x in range(0,t):
	n=int(input())
	a=set(list(str(n)))
	c=1
	if n==0:
		sys.stdout=open("out.txt","a")
		print("Case #"+str(x+1)+": "+"INSOMNIA")
		continue
	while(len(a)!=10):
		c=c+1
		b=set(list(str(n*c)))
		a=a|b
	sys.stdout=open("out.txt","a")
	print("Case #"+str(x+1)+": "+str(n*c))