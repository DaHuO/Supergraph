__author__ = 'bszikszai'

from io import *
import math

def getDivisor(i, primes):
    for j in primes:
        if j >= i:
            return None
        if i % j == 0:
            return j
    return None

def simulate(n, c):
    modLen = 2**(n - 2)
    primes = [2]
    resCtr = 0
    for i in range(3, 2**(n/2+1) - 1, 2):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    print "Primelist built"
    #print primes
    result = ''
    for i in range(0, modLen):
        num = 2**(n-1) + 2*i + 1
        bnum = '{0:b}'.format(num)
        divisors = []
        for j in range(2, 11):
            inum = int(bnum, j)
            divisor = getDivisor(inum, primes)
            if(divisor):
                divisors.append(divisor)
            else:
                #print str(num)+' is prime in ' + str(j) + ' - ' + str(inum)
                break
        if(len(divisors) == 9):
            result = result + '\n' + bnum + ' ' + ' '.join(map(str, divisors))
            resCtr = resCtr + 1
            if(resCtr == c):
                return result
    return result

def solve(f):
    inp = [int(x) for x in f.readline().rstrip('\n\r ').split(' ')]
    return simulate(inp[0], inp[1])

with open('input.txt', 'r') as f:
    with open('output.txt', 'wb') as g:
        cases = int(f.readline())
        for i in range(0, cases):
            solution = solve(f)
            print "Case #%s: %s" % (i+1, solution)
            g.write("Case #%s: %s\n" % (i+1, solution))