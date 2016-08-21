for t in xrange(int(raw_input())):
	print "Case #"+str(t+1)+":",
	n = int(raw_input())
	if (n==0):
		print 'INSOMNIA'
		continue
	c = [False]*10
	i = 1
	while(i):
		temp = n*i
		#print temp,
		while(temp>0):
			c[temp%10]=True
			temp = temp/10
		flag = 1
		for j in range(10):
			if (c[j]==False):
				#print n*i, c
				i+=1
				flag = 0
				break
		if (flag==1):
			break
	print i*n
	
