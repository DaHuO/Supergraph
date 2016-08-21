for z in range(int(input())):
	n=int(input())
	if n==0:
		print("Case #{}: INSOMNIA".format(z+1))
		continue
	d=[0]*10
	j=1
	while(True):
		a=list(map(int,str(n*j)))
		for i in a:
			d[i]=1
		if 0 not in d:
			break
		j+=1
	print("Case #{}: {}".format(z+1,n*j))


	
		
