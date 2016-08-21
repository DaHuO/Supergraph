









filer = open("B-large.in","r")
inp = filer.readline()
noc = int(inp)

filwrite = open("output2.txt","w")
op = ""

for i in range (1,noc+1):
	inp = filer.readline().strip()
	
	##### CODE HERE ######

	sol = 0
	ctr = 0
	for p in inp:
		if ctr == 0:
			currentchar = p
			previouschar = p
			ctr = 1
		else:
			previouschar = currentchar
			currentchar = p
		#print "current: %s, previous: %s" % (currentchar,previouschar)
		if currentchar != previouschar:
			sol+=1

	if inp[len(inp)-1]== '-':
			sol+= 1

	##### CODE END #######
	# print "Case #%d: "%i,
	# print sol

	op = op + ("Case #%d: " % i)
	op = op +  str(sol)
	op = op + "\n"

filwrite.write(op)
filer.close()
filwrite.close()
