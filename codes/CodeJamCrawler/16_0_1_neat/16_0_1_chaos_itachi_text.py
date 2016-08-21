
ss = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

bb = True
tc = int(raw_input())
for tc in xrange(1,tc+1):
	bx = int(raw_input())
	bxl = []
	for t in xrange(1,200):
		nbx = str(bx*t)
		nbx = list(nbx)
		bxl.extend(nbx)
		if set(bxl) == ss:
			bb = False
			break
	if bb == False:
		print  "Case #" + str(tc) + ":" + " " + "".join(nbx)
	elif bb == True:
		print "Case #" + str(tc) + ":" + " " + "INSOMNIA"
	
	