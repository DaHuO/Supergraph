import random

print "Case #1:"

def pow(a, b, m):
	d, t = 1, a
	while b!=0:
		if b%2==1:
			d = d*t%m
		b>>=1
		t = t*t%m
	return d

def witness(a, n):
 	d = n-1
 	while (d&1) == 0:
 		d>>=1
 	t = pow(a, d, n)
 	while d!=n-1 and t!=1 and t!=n-1:
 		t = t*t%n;
 		d <<= 1
 	return t==n-1 or (d&1)==1

def ok(n):
	if n==2:
		return True
	if n<2 or n%2==0:
		return False
	for i in range(20):
		a = random.randint(0, n-2)+1
		if witness(a, n) == False:
			return False
	return True

def get(a, b):
	res = 0
	size = len(a)
	for i in range(size):
		res = res * b + a[i]
	return res

def gcd(a, b):
	if b==0:
		return a
	return gcd(b, a%b)

def pollard_rho(n, c):
	i,k = 1, 2
	x = random.randint(0, n-2)+1
	y = x
	while True:
		i += 1
		x = (x*x%n+c)%n
		d = gcd(y-x, n)
		if 1<d and d<n:
			return d
		if y==x:
			return n
		if i==k:
			y=x
			k<<=1

def find(n, c, old):
	if n==1:
		return -1
	if ok(n):
		if n==old:
			return -1
		return n
	p = n
	while p>=n:
		p=pollard_rho(p, c)
		c -= 1
	v = find(p, c, old)
	if v!=-1:
		return v
	return find(n/p, c, old)
	find()

N, J = 16,50

n = N-2

All = (1<<n)

for i in range(All):
	a = [1]
	for j in range(n):
		if (i&(1<<j)) != 0:
			a.append(1)
		else:
			a.append(0)
	a.append(1)
	b, c = [], []
	for j in range(2, 11):
		b.append(get(a, j))
	tag = True
	for j in b:
		if ok(j) == True:
			tag = False
			break
		c.append(find(j, 12312, j))
	if tag:
		J -= 1
		x = reduce(lambda x, y: str(x)+str(y), a)
		b = c
		print ("%s %d %d %d %d %d %d %d %d %d" % (x, b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8]))
	if J==0:
		break

