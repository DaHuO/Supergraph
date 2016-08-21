for z in xrange(input()):
	n = input()
	if n != 0:
		x = map(str, range(10))
		m = n;
		while len(x) != 0:
			nn = list(str(m))
			for i in nn:
				if i in x:
					x.remove(i)
			m = m + n
		print "Case #"+str(z+1)+": "+str(m-n)
	else:
		print "Case #"+str(z+1)+": INSOMNIA"