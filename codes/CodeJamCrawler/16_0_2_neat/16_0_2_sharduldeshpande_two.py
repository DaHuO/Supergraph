count = 1

for _i in xrange(int(raw_input())):
	s = raw_input()
	x = ""
	z = s[::-1]
	for j in z:
		if(x=="" and j=="+"):
			continue
		elif(x=="" and j=="-"):
			x+=j
		elif(x[-1]==j):
			continue
		else:
			x += j
	print "Case #"+str(_i + 1)+": "+str(len(x))