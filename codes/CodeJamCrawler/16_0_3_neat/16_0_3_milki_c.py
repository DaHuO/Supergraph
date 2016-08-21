import random
from math import sqrt, ceil
import numpy

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

# print 'init'
# pp = primesfrom2to(1000000000)
# print 'init done'

pp = [2, 3, 5, 7, 11, 13, 17, 19]

def divisor(n):
    if n == 2:
        return 1
    max = n**0.5+1
    for i in pp:
        if i > max:
            return 1
        if n % i == 0:
            return i
    # while i <= max:
    #     if n % i == 0:
    #         return i
    #     i+=2
    return 1

def main():
    T = int(raw_input())
    for i in xrange(T):
        N, J = map(int, raw_input().split())
        #print N, J
        seen = set()
        ret = []
        while len(ret) < J:
            #st = ''.join(random.choice('01') for _ in xrange(N-3)) + '110'
            st = '1' + ''.join(random.choice('01') for _ in xrange(N-2)) + '1'
            if st in seen:
                continue
            seen.add(st)
            found = True
            t = [st]
            #print st
            for base in range(2, 11):
                i = int(st, base)
                #print "!", i,
                d = divisor(i)
                #print d
                t.append(d)
                if d == 1:
                    found = False
                    break
            if found:
                # print st
                ret.append(t)
        output(ret)

def output(ret, casenum=1):
    print 'Case #%d:' % casenum
    for n in ret:
        print ' '.join(map(str, n))


main()
