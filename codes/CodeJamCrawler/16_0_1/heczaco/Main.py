import math
f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

	
for t in xrange(T):
	N = int(f.readline())
	if (N==0):
		out = "Case #" + str(t+1) + ": INSOMNIA\n"
		
	else:
		i=0
		checked = [False,False,False,False,False,False,False,False,False,False]
		while checked != [True,True,True,True,True,True,True,True,True,True]:
			i=1+i
			for n in range(0,10):
				if str(n) in str(i*N):
					checked[n]=True		
			
		out = "Case #" + str(t+1) + ": " + str(i*N) + "\n"
	o.write(out)
	
	