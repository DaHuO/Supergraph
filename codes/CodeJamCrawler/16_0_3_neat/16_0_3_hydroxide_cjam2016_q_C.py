#!/usr/bin/python

import sys

# Pre-generate list of primes via trial division
primes = [2]
for j in range(3, int(1e6)):
    r = int(j**0.5)
    isPrime = True
    for p in primes:
        if j % p == 0:
            isPrime = False
            break
        elif p >= r:
            break
    if isPrime:
        primes.append(j)

print "Primes generated."

def getProof(jamcoin):
    proofs = []
    for i in range(2, 11):
        x = int(jamcoin, i)
        r = int(x**0.5)
        isPrime = True
        for p in primes:
            if x % p == 0:
                isPrime = False
                proofs.append(p)
                break
            elif p >= r:
                break
        if isPrime:
            return False
    return proofs


f = open(sys.argv[1])
o = open(sys.argv[2], 'w')
cases = int(f.readline())
for i in xrange(cases):
    o.write("Case #" + str(i+1) + ": \n")
    N, J  = map(int, f.readline().split())
    fstr  = '{:0' + str(N-2) + 'b}'
    for x in range(2**(N-2)):
        jamcoin = '1' + fstr.format(x) + '1'
        proofs  = getProof(jamcoin)
        if proofs:
            J = J-1
            print "Jamcoin found. " + str(J) + " remaining"
            o.write(jamcoin + ' ' + ' '.join(map(str, proofs)) + '\n')
        if J == 0:
            break

o.close()
print "Done, output written"
 
