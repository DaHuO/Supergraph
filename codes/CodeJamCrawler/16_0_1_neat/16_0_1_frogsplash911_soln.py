t = input()
for i in range(0,t):
	n = input()
	sn = n
	if n==0:
		print "Case #"+str(i+1)+": INSOMNIA"
	else:
		all = set()
		j=0
		while len(all) < 10:
			j+=1
			n=sn*j
			for c in str(n):
				all.add(c)
		print "Case #"+str(i+1)+": "+str(n)