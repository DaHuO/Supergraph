for i in range(input()):
	n=input()
	z=[0]*10
	if n==0:
		print "Case #"+str(i+1)+":",
		print "INSOMNIA"
	elif n==1:
		print "Case #"+str(i+1)+":",
		print 10
	else:
		b=1
		j=1
		while b:
			x=n*j
			y=map(int,str(x))
			for d in y:
				z[d]=1
			if 0 in z:
				j+=1
			else:
				b=0
		print "Case #"+str(i+1)+":",
		print x


