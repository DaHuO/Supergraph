import itertools
import time
import operator
# import collections
from collections import Counter
from itertools import repeat

inputFileName = "test.in"
inputFileName = "test2.in"

# inputFileName = "C-small-attempt0.in"
# inputFileName = "C-small-attempt1.in"
# inputFileName = "C-small-attempt2.in"

# inputFileName = "C-small-attempt3.in"
# inputFileName = "C-small-attempt4.in"

inputFileName = "C-large.in"
outputFileName = inputFileName[:-3] + ".out"

startTime = time.time()
print startTime


def calcPrimesFaster(N):
    max_odd = N / 2 + 1
    half_odds = [True] * max_odd
    for half in xrange(1, int(N ** 0.5 + 0.5) / 2 + 1):
        if half_odds[half]:
            prime = 2 * half + 1
            for j in range(2 * half * (half + 1), max_odd, prime):
                half_odds[j] = False
    res = [2]
    res.extend([2 * i + 1 for i in xrange(1, max_odd) if half_odds[i]])
    return res


def calcPrimes(N):
    primes = [2, 3, 5]
    for x in xrange(7, N / 2 * 2, 2):
        found = False
        for p in primes:
            if x % p == 0:
                found = True
                break
        if not found:
            primes.append(x)
    return primes


def convert(s, base):
    res = 0
    cur = 1
    for c in reversed(s):
        if c == '1':
            res += cur
        cur *= base
    return res


def checkPrime(x, primes):
    for p in primes:
        if x % p == 0:
            if x == p:
                return -1
            return p
    return -1


def calcSingleTest(f):
    line = f.readline()
    N = int(line.split()[0])
    J = int(line.split()[1])
    primes = calcPrimesFaster(10 ** 5)
    # primes = calcPrimes(10 ** 5)
    print "Primes = " + str(len(primes))
    res = []
    all = 0
    goodCnt = 0
    for i in xrange(0, 2 ** (N - 2)):
        all += 1
        rl = []
        s = (("{0:0" + str(N - 2) + "b}").format(i))
        s = '1' + s + '1'
        good = True
        for b in xrange(2, 11):
            v = convert(s, b)
            p = checkPrime(v, primes)
            if p == -1:
                good = False
                break
            else:
                rl.append(p)
        if good:
            goodCnt += 1
            res.append((s, rl))
            if len(res) >= J:
                break

    def convert_line(t):
        s, rl = t
        return s + ' ' + ' '.join(map(str, rl))
        # return s
        # return s + ' ' + '; '.join(map(lambda (x, i): str(convert(s, i)) + ' / ' + str(x) + ' = ' + str(convert(s, i) % x), zip(rl, xrange(2, 11))))

    print "all = {0}, good = {1}, p = {2}".format(all, goodCnt, float(goodCnt) / all)
    return '\n' + '\n'.join(map(convert_line, res))


with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            res = calcSingleTest(inpF)
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            print ' '
            outF.write('Case #{0}: {1}\n'.format(i, res))
            outF.flush()

print "Finished!!!! Total time = {0}".format((time.time() - startTime))
