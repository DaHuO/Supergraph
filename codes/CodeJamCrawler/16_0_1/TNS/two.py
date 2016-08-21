count = 1

for _i in xrange(int(raw_input())):
	s = raw_input()
	countp = 1
	cost = 0
	if(s[0]=="+"):
		flag = 0
	else:
		flag = 1
	for i in s:
		if(i=="+"):
			if(flag==0):
				countp += 1
			flag = 1
		elif(i=="-"):
			
			if(flag):
				cost += countp
			
			flag = 0

	print "Case #"+str(count)+": "+str(cost)
	count+=1