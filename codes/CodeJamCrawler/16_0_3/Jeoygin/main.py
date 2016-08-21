import sys
import numpy

def solve(f):
    strs = f.readline().split(' ')
    n = int(strs[0])
    j = int(strs[1])
    m = 0
    MAX = 100000
    is_prime = numpy.repeat(0, MAX + 1)
    primes = []
    i = 2
    while i < MAX:
        if is_prime[i] == 0:
            primes.append(i)
            d = i + i
            while d <= MAX:
                is_prime[d] = i
                d += i
        i = i + 1

    i = (1 << (n-1)) + 1
    while m < j:
        s = '{0:b}'.format(i)
        found_prime = False
        divisors = []
        for b in range(2, 11):
            d = int(s, b)
            if d <= MAX:
                if is_prime[d] == 0:
                    break
                else:
                    divisors.append(is_prime[d]);
            else:
                k = 0
                found = False
                while k < len(primes) and primes[k] * primes[k] <= d:
                    if d % primes[k] == 0:
                        found = True
                        divisors.append(primes[k])
                        break
                    k = k + 1
                if not found:
                    break
        if len(divisors) == 9:
            m = m + 1
            print s,
            for k in range(0,8):
                print divisors[k],
            print divisors[8]
        i = i + 2

if __name__ == "__main__":
   f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
   t = int(f.readline())
   for i in range(1, t + 1):
       print 'Case #%d:' % (i)
       solve(f)
