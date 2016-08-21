import isPrime
import random
from fractions import gcd
isp = isPrime.is_prime

def genNums(s):
    return [int(s,b) for b in range(2,11)]
	
def genStrs(a):
    x = a + 1
    while x < 2*a:
        yield "{0:b}".format(x)
        x += 2
		
def solve(lim, num):
	s = genStrs(2**lim)
	goods = []
	while len(goods) < num:
		t = s.next()
		p = genNums(t)
		if len([c for c in p if not isp(c)]) == 9:
			goods.append((t, [getDivisor(c) for c in p]))
			print t
	return goods
				
def getDivisor(N):
	if N%2==0:
			return 2
	y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
	g,r,q = 1,1,1
	while g==1:             
			x = y
			for i in range(r):
					y = ((y*y)%N+c)%N
			k = 0
			while (k<r and g==1):
					ys = y
					for i in range(min(m,r-k)):
							y = ((y*y)%N+c)%N
							q = q*(abs(x-y))%N
					g = gcd(q,N)
					k = k + m
			r = r*2
	if g==N:
			while True:
					ys = ((ys*ys)%N+c)%N
					g = gcd(abs(x-ys),N)
					if g>1:
							break
	 
	return g    
	
	
def solve16():
	x = solve(15, 50)
	o = open("jamcoin.small",'w')
	o.write("Case #1:\n")
	for y in x:
		o.write(y[0] + " " + " ".join([str(c) for c in y[1]]) + "\n")
	o.close()
	
	
def solve32():
	x = solve(31, 500)
	o = open("jamcoin.large",'w')
	o.write("Case #1:\n")
	for y in x:
		o.write(y[0] + " " + " ".join([str(c) for c in y[1]]) + "\n")
	o.close()