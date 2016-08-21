
t = int(raw_input(""))

for i in range(t):
	n = int(raw_input(""))
	if n==0:
		print "case #"+str(i+1)+": INSOMNIA"
		continue
		
	check = [False]*10
	j = 0
	
	while False in check:
		j+=1
		s = str(j*n)
		for c in s:
			check[int(c)] = True
			
	
	print "case #"+str(i+1)+": "+str(j*n)

