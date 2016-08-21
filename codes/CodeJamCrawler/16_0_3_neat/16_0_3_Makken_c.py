import itertools
import math

# Returning the divisor
def is_not_prime(n):
    if n == 2:
        return False
    if n % 2 == 0 or n <= 1:
        return 2

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return divisor
    return False

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

preGenPrimeTable = rwh_primes(10000000)

def createJamCoin(digits, cases):
    o = open("output.txt", "w")
    o.writelines("Case #1:\n")
    count = 0
    iterObj = itertools.product('01', repeat=digits - 2)
    while count < cases:
        currentStr = "1"+ "".join(iterObj.next()) + "1"
        list1 = [int(currentStr, currentBase) for currentBase in range(2, 11)]#  + listOfAdditions[currentBase - 2] for currentBase in range(2, 11)]
        currentDivisors = []

        for item in list1:
            for prime in preGenPrimeTable:
                if item % prime == 0 and item != prime:
                    currentDivisors.append(str(prime))
                    break

        if len(currentDivisors) == 9:
            o.writelines("{} ".format(currentStr) + " ".join(currentDivisors) + "\n")
            count+=1

createJamCoin(32,500)
