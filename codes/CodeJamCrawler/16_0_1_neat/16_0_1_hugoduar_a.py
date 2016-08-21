t = int(raw_input())
for y in range(t):
	td = 0
	ht = [0 for x in range(10)]
	N = raw_input()
	NA = N
	i = 2
	flag = True
	while td<10:
		for x in NA:
			if ht[int(x)] == 0: 
				td+=1
			ht[int(x)] += 1
			
		if int(N)*i == int(N): 
			print "Case #%s: INSOMNIA" % str(y+1)
			flag = False
			break
		elif td==10:  print "Case #%s: %s" % (str(y+1), str(int(N)*(i-1)))
		NA = str(int(N)*i)
		i+=1
	t-=1  	