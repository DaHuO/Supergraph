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

o=open('out',"w+")
f=open('A-large.in')
n=int(f.readline())
i=1
while i<=n:
	o.write("Case #"+str(i)+": "+pa(int(f.readline().strip()))+"\n")
	i+=1
f.close()
