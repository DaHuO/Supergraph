import sys, math,itertools
lines = sys.stdin.readlines()
write = sys.stdout.write
def solve(n,j):
	#midlst = list(itertools.product([0, 1], repeat=n-2))
	res=[]
	l = 2**30-1
	while len(res)<j:
		tmpn = '1'+'{0:030b}'.format(l)+'1'
		tmplst=[tmpn]
		for i in range(2,11):
			convertN = genN(tmpn, i)
			prime,divisor=is_prime(convertN)
			#print tmplst,convertN,l,divisor
			if prime:
				tmplst=[]
				break
			if not prime:
				tmplst.append(divisor)
		if len(tmplst):
			#print tmplst, convertN
			res.append(tmplst)
		l-=1

	return '\n'.join([' '.join(map(str,x)) for x in res])


def genN(n, b):
	res=b**(len(n)-1)+1
	for i in range(1,len(n)-1):
		#print n[i],b**(len(n)-1-i)
		res+=0 if n[i]=='0' else b**(len(n)-1-i)
	return res


def is_prime(n):
    if n == 2:
        return [True,None]
    if n % 2 == 0 or n <= 1:
    	#print 'divisor',2
        return [False,2]

    sqr = int(math.sqrt(n)) + 1
    limit = 1000000
    for divisor in range(3, limit, 2):
        if n % divisor == 0:
            return [False,divisor]
    return [True,None]

	

t = int(lines[0])
for i in range(1,t+1):
	#print 'lines',lines[i],type(lines[i])
	N,J=map(int,lines[i].replace('\n','').split(' '))
	res = solve(N,J)
	res = str(res)
	write('Case #%d:\n%s\n'%(i,res))