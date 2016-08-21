# To change this template, choose Tools | Templates
# and open the template in the editor.

#__author__="Mukesh Tiwari"
#__date__ ="$Feb 10, 2010 1:35:26 AM$"

from __future__ import print_function

import random
from Queue import Queue
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def is_probable_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
 
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(10):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

def rabin_miller(p):
	if(p<2):
		return False
	if(p!=2 and p%2==0):
		return False
	s=p-1
	while(s%2==0):
		s /= 2
	for i in xrange(20):
		a=random.randrange(p-1)+1
		temp=s
		mod=pow(a,temp,p)
		while(temp!=p-1 and mod!=1 and mod!=p-1):
			mod=(mod*mod)%p
			temp=temp*2
		if(mod!=p-1 and temp%2==0):
			return False
	return True
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

#if __name__ == "__main__":
ntest = input()
for tc in range(ntest):
    print("Case #", end = "")
    print(tc + 1, end = "")
    print(":")
    N = input()
    cnt = input()
    for i in range(2 ** (N - 2)):
        base = []
        numb = []
        bina = []
        for s in range(2, 11):
            base.append(s)
            numb.append(0)
        at = 0
        cur = i
        for t in range(N - 2):
            bina.append(cur % 2)
            if (cur % 2 == 1):
                for s in range(len(numb)):
                    numb[s] += base[s]**at
            cur /= 2
            at += 1
        ok = True
        for s in range(len(numb)):
            numb[s] = numb[s] * base[s] + 1 + (base[s] ** (N - 1))
            if (is_probable_prime(numb[s])):
                ok = False
                break
        if (ok == True):
            cnt -= 1
            print(1, end = "")
            for dig in range(N - 3, -1, -1):
                print(bina[dig], end = "")
            print(1, end = "")
            print(" ", end = "")
            for s in range(len(numb)):
                print(brent(numb[s]), end = " ")
            print("")
            if (cnt == 0):
                break