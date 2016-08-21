t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n = int(raw_input())
	if n == 0:
		print "Case #{}: INSOMNIA".format(i)
		continue
	list = [0]*10
	j=1	
	while any(x==0 for x in list):
		newvar=n*j
		j=j+1
		m=newvar
		while m!=0:
			temp=m%10
			m=m/10
			list[temp]=1
	print "Case #{}: {}".format(i,newvar)