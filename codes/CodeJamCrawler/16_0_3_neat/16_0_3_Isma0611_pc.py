import numpy as np
import random
def getd(n):
   a = np.array([],dtype=int)
   while n:
       a, n = np.append(a , n % 10), n // 10
   return a


def primet(a):
    # return all(a % i for i in xrange(2, a))
    for i in xrange(2, int(np.sqrt(a))+1):
    	if a%i==0: return i
    return 0

def pc(n):
	s='1'+''.join([random.choice('10') for x in range(n-2)])+'1'

o=open('out',"w+")
f=open('in')
n=int(f.readline())
i=1
n,j=f.readline().split()
n,j=int(n),int(j)
closed=np.array([], dtype=int)
o.write('Case #1: \n')
while i<=j:
	s='1'+''.join([random.choice('10') for x in range(n-2)])+'1'
	d=int(s)
	if d not in closed:
		closed=np.append(closed,[d])
		ps=np.array([], dtype=int)
		skip=True
		for x in [2,3,4,5,6,7,8,9,10]:
			p=primet(int(s,x))
			if(not p): 
				skip=False
				break
			ps=np.append(ps,[p])

		if skip:
			ps=" ".join([str(k) for k in ps])
			# print("Case #"+str(i)+": "+s+" "+ps)
			o.write(s+" "+ps + "\n")
			i+=1
f.close()
