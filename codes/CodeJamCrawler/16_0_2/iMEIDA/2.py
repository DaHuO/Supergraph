for z in xrange(input()):
	c = 0
	o = raw_input()+' '
	o2 = list()
	temp = o[0]
	for i in o[1:]:
		if i != temp:
			o2.append(temp)
			temp = i
	for i in range(len(o2[:-1])):
		if o2[i] != o2[i+1]:
			c = c + 1
			for j in range(0, i+1):
				o2[j] = o2[i+1]
	if o2[-1] == '-':
		c = c + 1
	print "Case #"+str(z+1)+": "+str(c)