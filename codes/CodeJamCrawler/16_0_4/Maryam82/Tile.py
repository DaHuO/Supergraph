inF = open('D-small-attempt0.in.txt','r')
ouF = open('MaryamQD.out','w')

content = inF.read().splitlines()
t, output   = int(content[0]), ''
for i in xrange(1, t + 1):
	K, C, S =  map(int, content[i].split())
	output += "Case #%d: " %i 
	for j in xrange(1,S +1):
		output += '%d ' % (j*pow(K,C-1))
	output += '\n'

ouF.write(output)
ouF.close()
