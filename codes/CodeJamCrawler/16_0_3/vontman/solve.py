import math
def isprime(x):
	if(x < 2):
		return 0;
	iter = 0
	for i in xrange(2,(int)(math.sqrt(x))+1):
		if iter > 100:
			return 0
		if x%i == 0:
			return i
		iter+=1
	return 0
with open('test.in','r') as inp:
	t,n,j = map(int,inp.read().split())
temp = [ 1+i**(n-1) for i in xrange(2,11) ]
ts = [0 for i in range(2,11)]
mask = 0
out = open('test.out','w')
out.write("Case #1:\n")
while j > 0:
	flag = False
	tmp = 0 
	for i in xrange(9):
		added = 0
		for k in xrange(1,n-1):
			if mask&(1<<(k-1)):
				added += (i+2)**k
		tmp = added+temp[i]
		ts[i] = isprime(tmp)
		if ts[i] == 0:
			flag = True
			break
	if not flag :
		j-=1
		out.write(str(tmp) )
		out.write(" ")
		out.write(" ".join(map(str,ts)))
		out.write("\n")
	mask+=1
out.close()
	
