def evacuate(nparty, ns):
	party = chr(ord('A') + nparty)
	res = ""
	for i in xrange(0, ns / 2):
		res += party *2 + " "
	if (ns % 2 == 1):
		res += party + " "
	return res	
		
 


inf = open("a.in", 'r')
outf = open("a.out", 'w')

t = int(inf.readline())

for k in xrange(0, t):
	n = int(inf.readline())	
	p = map(int, inf.readline().split())
	if (p[0] >= p[1]):
		maxvp = 0
		sndmaxvp = 1
	else:
		maxvp = 1
		sndmaxvp = 0
	outf.write("Case #" + str(k + 1) + ": ")	
	for i in xrange(2, n):
		if p[i] >= p[maxvp]:
			sndmaxvp = maxvp
			maxvp = i
		elif p[i] > p[sndmaxvp]:
			sndmaxvp = i
	#print k, maxvp, sndmaxvp
	d = p[maxvp] - p[sndmaxvp]
	outf.write(evacuate(maxvp, d))
	for i in xrange(0, n):
		if (i <> maxvp) and (i <> sndmaxvp):
			outf.write(evacuate(i, p[i]))
	mvp_letter =  chr(ord('A') + maxvp)
	smvp_letter =  chr(ord('A') + sndmaxvp)
	for i in xrange(0, p[sndmaxvp]):
		outf.write(	mvp_letter + smvp_letter + " ")
	outf.write("\n")
		
			
	#print evacuate("A", 5)
	#outf.write(str(sleeping_number(n)) + "\n")
outf.close()
