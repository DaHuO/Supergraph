for i in range(1,input()+1):
	n=input()
	d=dict.fromkeys(range(0, 10), 0)
	c=0
	for j in range(1,101):
		k=n*j	
		while(k>0):
			d[k%10]=d[k%10]+1
			k=k/10
		if 0 not in d.values():
			print "Case #{0}: {1}".format(i,n*j)
			c=1
			break
	if c==0:
		print "Case #{0}: {1}".format(i,'INSOMNIA')


		



	#