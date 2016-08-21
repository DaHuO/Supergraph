import numpy as np 

T = raw_input('')
for i in np.arange(0,int(T),1):
	s = raw_input('')
	if s[0]=='-':
		total = 1
		sur = (s.split("+")[0]).count("-")
	else:
		total = 0
		sur = 1
	l =  s[sur:].split("+")
	l = [y for y in l if y != '']
	#print l
	total = total + 2*len(l)
	print "Case #"+str(i+1)+":", total