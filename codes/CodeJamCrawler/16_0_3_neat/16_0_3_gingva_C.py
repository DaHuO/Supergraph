def parseScalar(f,c=int):
    return c(f.next().strip('\r\n'))
def parseTuple(f,c=int):
    return tuple(c(s) for s in  f.next().strip('\r\n').split())

import time
def main(fn1, fn2):
    startTime = time.time()
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            ncases = parseScalar(f)
            for n in range(ncases):
                N,J = parseTuple(f)
                print N,J
                x = solveRand(N,J)
                print>>g, 'Case #%d:'  % (n+1)
                print 'Case #%d: %s'  % (n+1,str(x)  )
                for s,facts in x:
                    print>>g, '%s %s'%(s, ' '.join(str(x) for x in facts))
                    print '%s %s'%(s, ' '.join(str(x) for x in facts))
    print 'Computed in %d seconds'%(time.time()-startTime)


import sys, random, math
def pickRandom01(n): # uniform, TODO may be better to pick larger numbers ie higher prob on the left as less primes there
    return [1*(random.random()>0.5) for i in xrange(n)]
def firstFactor(n):
    if n % 2 == 0 :
        return 2
    sqr = min(int(math.sqrt(n)) + 1, 1530827) # retry rather than spend ages confirming primality
    for divisor in xrange(3, sqr, 2): #todo iter over primes?
        if n % divisor == 0:
            return divisor
    return 0

def number(idx,base):
    N = len(idx)
    return sum(idx[j]*base**(N-j-1) for j in xrange(N))

def solveRand(N,J):
    results = []
    idxStrAll = set() # very unlikely we would hit the same 16 or 32 binary word over 50 or 500 samples but let's not risk it
    for i in xrange(J):
        print 'finding result ',i
        while True:
            idx = pickRandom01(N-2)
            idx = [1] + idx + [1]
            idxStr = ''.join(str(i) for i in idx)
            if idxStr in idxStrAll :
                continue
            numbers = [number(idx,base) for base in xrange(2,11)]
            factors = []
            for n in numbers:
                f = firstFactor(n)
                if f == 0 or f == n or f == 1:
                    break
                factors.append(f)
            if len(factors) <> 9:
                continue
            print idxStr, factors
            #double check
            sr = idx[-1::-1]
            for i,f in enumerate(factors):
                    b = i+2
                    val = sum(b**k*v for k,v in enumerate(sr))
                    assert(val == numbers[i])
                    if f == 0 :
                        break
                    assert(f <> 1 and f<>val and val%f == 0)
            else:
                res = (idxStr, factors)
                idxStrAll.add(idxStr)
                print
                print numbers
                print res
                results.append(res)
                assert(len(factors)==9)
                break
    return results


if __name__ == '__main__':
    #solveRand(16,50)
    #main('C-test.in', 'C-test.out')
    #main('C-test-large.in', 'C-test-large.out')
    main('C-small-attempt0.in', 'C-small-attempt0.out')
    main('C-large.in', 'C-large.out')
    sys.exit(0)


