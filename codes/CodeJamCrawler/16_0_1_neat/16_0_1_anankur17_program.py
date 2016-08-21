EVER = 6
t = input()
for a in range(1,t+1):

	n = input()
	se = set()
	mul = 0
	while mul<=pow(10,EVER):
		mul+=1
		if len(se) == 10:
			break
		ans = mul*n
		#print mul,ans
		se = se.union(list(str(ans)))
	if mul>pow(10,EVER):
		print "Case #"+str(a)+": "+"INSOMNIA"
	else:
		print "Case #"+str(a)+": "+str((mul-1)*n)
