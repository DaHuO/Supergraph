for x in range(int(input())):
	n=int(input())
	i=2
	s=set()
	q=1
	sum=0
	if n==0:
		print("Case #"+str(x+1)+": INSOMNIA")
	else:
		for j in str(n):
			s.add(int(j))
			sum=sum+int(j)
		for e in s:
			q=e
			break
		if q==0 and sum==45:
			print("Case #"+str(x+1)+": "+str(n))
			break
		while(True):
			sum=0
			n1=i*n
			for j in str(n1):
				s.add(int(j))
			for f in s:
				sum=sum+f
			for e in s:
				q=e
				break
			if q==0 and sum==45:
				print("Case #"+str(x+1)+": "+str(n*i))
				break
			i+=1