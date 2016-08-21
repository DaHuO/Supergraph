import numpy as np
def getd(n):
   a = np.array([],dtype=int)
   while n:
       a, n = np.append(a , n % 10), n // 10
   return a


def pa(n):
	if n==0: return "INSOMNIA"
	d=np.array([],dtype=int)
	i=1
	while(d.shape[0]<10):
		d=np.unique(np.concatenate((getd(n*i),d)))
		i+=1
	return str(n*(i-1))

def pb(st):
	a=np.array([], dtype=bool)
	for s in st:
		if( "+" ==s): a=np.concatenate((a, [True]))
		else: a=np.append(a, [False])
	nb=0;
	l=len(a)+1
	while (not a.all()):
		for i in xrange(1,l):
			if(not a[-1*i]):
				a[:l-i]=np.invert(a[:l-i])
				nb+=1
				break
	return str(nb)


o=open('out',"w+")
f=open('B-large.in')
n=int(f.readline())
i=1
while i<=n:
	o.write("Case #"+str(i)+": "+pb(f.readline().strip())+"\n")
	# print("Case #"+str(i)+": "+pb(f.readline().strip())+"\n")
	i+=1
f.close()
