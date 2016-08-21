t = input()
for m in range(t):
	a = list(xrange(10))
	n = input()
	flag = 0
	b = 0
	
	if n != 0:
		for i in range (1,1000001):
			s = i*n
			if flag == 1:
				break
			b=s
			for j in str(s): 
				#print j
				a[int(j)-1] = 0 
				#print a
				if sum(a) == 0: 
				 	flag = 1 
				 	break
	
	if flag == 0: 
		print "Case #%d: INSOMNIA" % (m+1) 
	else: 
		print "Case #%d: %d" % (m+1,b)