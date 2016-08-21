from itertools import permutations

def pr(s):
	ret = []
	for i in range(2,11):
		x = int(s,i)
		for t in range(2,101):
			if x%t==0 and x!=t:
				ret.append(t)
				break
	return ret

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
    	if sieve[i]:
    		k=3*i+1|1
        	sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        	sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

p = set(primes2(10**7+1))

T = input()
N,c = map(int,raw_input().split())

print "Case #1: "
t = ''.join(['1'] + ['0'] * 14 + ['1'])
while c > 0:
	l = map(int,pr(t))
	if len(l)!=9: 
		t = bin(int(t,2)+2)[2:]
		continue
	print t + " " + ' '. join(map(str,l))
	t = bin(int(t,2)+2)[2:]
	c -= 1