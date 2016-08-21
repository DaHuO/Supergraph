'''
Created on 8 Apr 2016

@author: Andy
'''
def solveProblem(n,j):
    """
    """
    primes = list(loadPrimes())
    for n in xrange( pow(2,n-1) + 1, pow(2,n),2):
        binNumber = bin(n)[2:]
        factors = []
        for base in xrange(2,11):
            firstFactor = findFirstFactor(int(binNumber,base), primes)
            if not firstFactor:
                continue
            factors.append(firstFactor)
        if len(factors) == 9:
            print binNumber + " " + " ".join(map(str,factors))
            j -= 1
            if j == 0:
                break
    
def loadPrimes():
    """
    Read the prime numbers from a file.
    """
    with open('primesTo10000.txt') as primeFile:
        for prime in primeFile.readline().split(','):
            yield int(prime)
            
def findFirstFactor(n, primes):
    """
    Find the first prime number factor of a number
    """
    for p in primes:
        if p >= n:
            break
        if n % p == 0:
            return p
    return None
	
if __name__ == '__main__':

    with open('problem.txt') as fp:
        solveProblem(16,50)
        