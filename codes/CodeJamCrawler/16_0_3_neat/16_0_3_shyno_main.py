'''
Coin Jam
'''
import math
import itertools


def isprime(n):
    """Returns True if n is prime and False otherwise"""
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    f = open("C-small-attempt0.in")
    nc = int(f.readline())
    for x in xrange(1, nc+1):
        (n, j) = map(int, f.readline().strip('\n').split(' '))
        print "Case #%d:" % (x)
        for s in map(''.join, itertools.product('01', repeat=n-2)):
            jc = '1' + s + '1'
            isjamcoin = True
            nontriv = []
            for i in range(2, 11):
                if isprime(int(jc, i)):
                    isjamcoin = False
                    break
            if isjamcoin:
                for i in range(2, 11):
                    b = int(jc, i)
                    k = 2
                    while b % k != 0:
                        k += 1
                    nontriv.append(b / k)
                print "%s %s" % (jc, ' '.join(map(str, nontriv)))
                j -= 1
            if j == 0:
                break
