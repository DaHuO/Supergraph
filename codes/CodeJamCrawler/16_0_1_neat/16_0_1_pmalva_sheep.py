T = int(raw_input())

for i in xrange(T):
	numbers = [False for j in xrange(10)]
	N = int(raw_input())
	v = N	
	
	while v>0:
		for digit in str(v):
			numbers[int(digit)] = True
		
		if False not in numbers:
			print "Case #"+str(i+1)+":",v
			break

		v += N

	if v==0:
		print "Case #"+str(i+1)+": INSOMNIA"
