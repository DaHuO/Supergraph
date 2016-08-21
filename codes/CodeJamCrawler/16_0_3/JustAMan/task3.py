import sys
import struct

def solve(n, j):
    # primes.32b is taken from http://www.umopit.ru/CompLab/primes32.htm
    with open('primes.32b', 'rb') as primesFile:
        if n < 32:
            primes = (2,) + struct.unpack('I' * 10000, primesFile.read(10000 * 4))
        else:
            assert False, 'not yet supported'
    start = int('1%s1' % ('0' * (n - 2)), 2)
    topmost = int('1' * n, 2)
    checkPrimes = set(x for x in primes if (x >= start) and (x <= topmost))
    #print len(primes)

    def isCoin(num):
        for base in range(2, 10 + 1):
            if int(num, base) in checkPrimes:
                return False
        return True

    def makeNum(middle):
        binMiddle = ('0' * n + bin(middle)[2:])[-(n - 2):]
        return '1%s1' % binMiddle

    def findDivisor(x):
        for p in primes:
            if x % p == 0:
                return str(p)
        raise ValueError('Expected non-prime argument')

    def getDivisors(num):
        return [findDivisor(int(num, base)) for base in range(2, 10 + 1)]

    result = ['']
    middle = 0
    while j > 0:
        num = makeNum(middle)
        if isCoin(num):
            try:
                result.append(' '.join([num] + getDivisors(num)))
            except ValueError:
                # not a coin
                pass
            else:
                j -= 1
        middle += 1

    return '\n'.join(result)
    #print len(set(result))
    #print start

def main(inFile):
    with open(inFile) as inp, open(inFile.replace('.in', '.out'), 'w') as out:
        T = int(inp.readline().strip())
        for t in xrange(T):
            N, J = [int(x) for x in inp.readline().strip().split()]
            out.write('Case #%d: %s\n' % (t + 1, solve(N, J)))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: %s input.in' % sys.argv[0])
    main(sys.argv[1])
