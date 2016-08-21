def f(s):
	 
	s = s.rstrip('\n')
	c= s[0]
	s = s + "+"
	if s[0]=="-":
		res = 0
	else:
		res = 0
	
	for ct in list(s):
		if (c != ct):		
			res	 += 1
		c = ct
	return res 	
    
from sys import stdin

def r():
    return stdin.readline()
for cn in range(int(r())):
    d = r()
    print ("Case #%d: %d"%(1+cn,f(d)))
	
	
	 