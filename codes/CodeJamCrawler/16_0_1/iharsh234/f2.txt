for x_ in xrange(int(raw_input())):
	n = input()
	i = 1
	n1 = n
	a = set()
	while n != 0:
		#print n1
		for x in list(str(n1)):
			a.add(x)
		if len(a) == 10:break
		n1 = n*(i+1)
		i += 1
	if n != 0:print 'Case #'+str(x_+1)+':',n*i
	else:print 'Case #'+str(x_+1)+':','INSOMNIA'