def is_prime(num):
	if num==2:
		return 2
	if num<=1:
		return 1
	if num%2==0:
		return 2
	for i in xrange(3,int(num**0.5) +1,2):
		if num%i==0:
			return i
	return 1

def func(n):
	s = n
	for i in xrange(2,11):
		k = is_prime(int(n,i))
		if k==1:
			return None
		s+= " "+ str(k)
	return s

def fun(p,j):
	k = 0
	n =2**(p)
	m = 2**(p-1)
	for i in xrange(m+1,n,2):
		if k==j:
			return
		p = func(bin(i)[2:])
		if p:
			print p
			k+=1



f = open('B-small-practice.in','r')
n = int(f.readline())
# g = open("aaaa.txt","w")
for i in range(n):
	a = map(int,f.readline().split())
	print "Case #"+str(i+1)+":"
	fun(a[0],a[1])
# g.close()
f.close()


