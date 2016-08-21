def sleepsheep(a,n,p):
	print "Case #{}:".format(p),
	j=1
	flag=0
	while(not all(a)):
		for i in str(j*n):
			a[int(i)]+=1
		j+=1
		if n==j*n:
			print "INSOMNIA"
			flag=1
			break
	if not flag:print (j-1)*n

t=int(raw_input())

p=1
while(p<=t):
	n=int(raw_input())
	sleepsheep([0]*10,n,p)
	p+=1
