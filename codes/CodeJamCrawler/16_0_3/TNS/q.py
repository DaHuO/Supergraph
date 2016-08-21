def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            if(len(primfac)>2):
            	return primfac
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


for _i in xrange(int(raw_input())):
	n,j = map(int,raw_input().split())
	ini = 32769
	fin = 65535
	count = 0
	f = 1
	for i in xrange(ini,fin+1,2):
		b = bin(i)
		b = b[2:]
		base = []
		temp = []
		for j in xrange(2,11):
			base.append(int(b,j))

		for j in base:
			x = primes(j)
			temp.append(x[0])
		##print temp
		##print base
		flag = 1
		for i in xrange(len(base)):
			if(temp[i]==base[i]):
				flag = 0
				break
		if(flag!=0):
			print b,
			for i in temp:
				print i,
			print ""
			count+=1
			if(count==j):
				f = 0
				break
		if(f==0):
			break

