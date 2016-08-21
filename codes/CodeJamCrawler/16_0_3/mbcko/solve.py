#!/usr/bin/env python

import sys

#@profile
def isPrime(n):
    if n == 2 or n == 3: return True, None
    if n < 2 or n%2 == 0: return False, 2
    if n < 9: return True, None
    if n%3 == 0: return False, 3
    r = int(n**0.5)
    f = 5
    while f <= r:
        # filter too big numbers
        if f > 1000: return True, None
        
        if n%f == 0: return False, f
        if n%(f+2) == 0: return False, f+2
        f +=6
    return True, None
    

#@profile
def solve(*args):
    (N, J) = args
    
    retval = []
    first = int("1" + "0" * (N-2) + "1", 2)
    last = int("1" * N, 2)
    
    for n in xrange(first, last + 1, 2):
        prime = False

        ret = [bin(n)[2:]]
        for b in range(2, 11):
            nb = int(bin(n)[2:], b)
            
            wasPrime = isPrime(nb)
            prime |= wasPrime[0]
            ret.append(wasPrime[1])
            if prime:
                continue
            
        if not prime:
            retval.append(ret)
            print >> sys.stderr, len(retval), ret[0]
            
        if len(retval) == J:
            break
    
    return "\n" + "\n".join(list(" ".join(map(str, one)) for one in retval))

def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
        params = [int(one.strip()) for one in sys.stdin.readline().split(" ")]
        result = solve(*params)
        print "Case #%d: %s" % (caseNumber, result)
       
if __name__ == '__main__':
    main()


