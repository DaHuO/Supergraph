def isPrime(n):
	i = 2
	while (i*i<=n):
		if (n%i==0):
			return i
		else:
			i+=1
	return -1
def func(x):
	# convert x to different bases
	# check if its prime or not
	#print x[::-1], "=>",
	l = len(x)
	ans = []
	for i in range(2,11):
		temp = 0
		for j in range(l):
			if (x[j]=='1'):
				temp+=(i**j)
		#print temp,
		#check is temp is prime
		z = isPrime(temp)
		if (z==-1):
			#print ""
			return False
		else:
			ans.append(z)
	#print ""
	w = str(x[::-1])
	for i in ans:
		w += (" "+ str(i))
	print w
	return True
	
	
	
for t in xrange(int(raw_input())):
	print "Case #"+str(t+1)+":"
	n, j = map(int, raw_input().split())
	n -= 2
	for i in range(2**n):
		b = bin(i)[2:]
		l = len(b)
		m = '1'+'0'*(n-l)+b+'1'
		rev = m[::-1]
		if (func(rev)):
			j-=1
			if (j==0):
				break
		
