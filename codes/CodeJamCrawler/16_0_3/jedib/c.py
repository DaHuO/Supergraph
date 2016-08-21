#!/usr/bin/python
import math

nb = int(raw_input())

def find_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes = find_primes(2**16)

print "Case #%i:" % (nb)

N, J = [int(i) for i in raw_input().split()]

start = 2**(N-1) + 1
end = 2**(N)

count = 0

for i in xrange(start, end):
    if i % 2 == 0:
        continue
    chaine = bin(i)[2:]
    #print ''
    #print chaine
    dico = {}
    for base in xrange(2, 11):
        nb = int(chaine, base)
        #print "base =", base, "  ", nb

        maxDiv = int(math.sqrt(nb))
        divisible = False
        for div in primes:
            if div > maxDiv + 1:
                break;
            if nb % div == 0:
                #print nb, 'is divisible by', div
                divisible = True
                dico[base] = str(div)
                break
		if divisible == False:
			break

    #print dico
    if len(dico) == 9:
        print chaine, " ".join(dico.values())
        count += 1
        if count == J:
			break
