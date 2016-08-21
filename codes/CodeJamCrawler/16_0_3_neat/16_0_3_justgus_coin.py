import random
from fractions import gcd 

def brent(N):
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
def pollardRho(N):
        if N%2==0:
                return 2
        x = random.randint(1, N-1)
        y = x
        c = random.randint(1, N-1)
        g = 1
        while g==1:             
                x = ((x*x)%N+c)%N
                y = ((y*y)%N+c)%N
                y = ((y*y)%N+c)%N
                g = gcd(abs(x-y),N)
        return g
				
N = 16
J = 50

found = 0

print("Case #0:")

for i in range(2**(N-2)):

	temp = []
	
	numstr = "{0:b}".format(2*i + 1 + 2**(N-1))
	
	temp.append(numstr)
	
	for j in range(2,11):
		
		# number interpreted as base j.
		num_in_base = int(numstr, j)
		
		divisor = brent(num_in_base)
		
		if divisor == num_in_base: 
			break
		
		temp.append(divisor)
		
	if len(temp) == 10: print(" ".join(str(x) for x in temp))
	
	if found >= J: break
	
	