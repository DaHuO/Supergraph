import numpy as np

for i in range(input()):
	n=input()
	a=[[0 for x in range(n)] for x in range(2*n-1)]
	for x in range(2*n-1):
		a[x]=map(int,raw_input().split())
	print "Case #"+str(i+1)+":",
	a=np.array(a)
	#print a
	c=list(a.flatten())
	#print c
	b=[]
	for j in range(len(c)):
		if c.count(c[j])%2!=0:
			b.append(c[j])
			#c.remove(c[j])
	b= list(set(b))
	b.sort()
	for q in b:
		print q,
	print