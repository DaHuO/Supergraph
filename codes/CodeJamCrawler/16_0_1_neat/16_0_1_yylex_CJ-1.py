T = input ()
for i in xrange (T):
	N = input ()
	if N == 0:
		print "Case #"+str(i+1)+": INSOMNIA"
	else :
		j = 1
		digits = set ()
		num = N
		while 1 :
			digits |= set(list(str(num*j)))
			if len(digits) == 10 :
				print "Case #"+str(i+1)+": "+str(num*j)
				break
			j += 1