t = input()
for j in xrange(t):
	n = input()
	ans = 0
	d = [0]*10
	if n == 0:
		ans = "INSOMNIA"
	else:
		i=1
		while(sum(d)!=10):
			temp = i*n
			while (temp!=0):
				d[temp%10]=1
				temp= temp/10
			i+=1
		ans = (i-1)*n
	print "Case #{}: {}".format(j+1,ans)
