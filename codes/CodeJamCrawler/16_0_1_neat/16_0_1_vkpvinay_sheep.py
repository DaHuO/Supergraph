for i in range(1,int(input())+1):
	n=input()
	if n=='0':
		print("Case #{}: {}".format(i, 'INSOMNIA'))
	else:
		j=n1=int(n)
		c=set(n)
		while True:
			n1+=j
			n=str(n1)
			c=c.union(set(n))
			#print(n1)
			if len(c)==10:
				break;
		print("Case #{}: {}".format(i,n1))