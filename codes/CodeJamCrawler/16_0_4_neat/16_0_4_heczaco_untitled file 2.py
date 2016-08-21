import math
f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

	
for t in xrange(T):
	p= map(int, f.readline().strip().split(' '))
	asda = p[0]
	k = p[1]
	s = p[2]
	strOut =""
	for i in range(1,s+1):
		strOut= strOut + " " + str(i) 
		
	out = "Case #" + str(t+1) + ": " + strOut + "\n"
	print out
	o.write(out)
	
	