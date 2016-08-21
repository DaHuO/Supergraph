T = int(raw_input())
for i in xrange(T):
	N = int(raw_input())
	if N == 0:
		print "Case #%d: INSOMNIA" %(i+1)
	else:
		seen = [0,0,0,0,0,0,0,0,0,0]
		coef = 1
		while True:
			cur = str(coef*N)
			for char in cur:
				seen[int(char)]=1
			flag = False
			for elem in seen:
				if elem == 0:
					flag = True
			if flag == False:
				print "Case #%d: %s" %(i+1,cur)
				break
			else:
				coef+=1



