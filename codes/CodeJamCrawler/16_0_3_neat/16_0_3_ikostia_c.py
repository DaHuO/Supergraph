import math
import datetime

primes = []
def build_primes(m):
    global primes
    primes = [2,3]
    for i in xrange(5, m, 2):
        s = int(math.sqrt(i) + 1)
        j = 0
        prime = True
        while j < len(primes) and primes[j] <= s and prime:
            if i % primes[j] == 0:
                prime = False
            j = j + 1
        if prime:
             primes.append(i)

def non_triv_div(k):
    s = int(math.sqrt(k) + 1)
    for p in primes:
         if p >= s:
             break
         if k % p == 0:
             return p 
    return 1

def fits(m):
    bm = bin(m)[2:]
    divs = []
    for base in xrange(2, 11):
        k = int(bm, base)
        divs.append(non_triv_div(k))
        if divs[-1] == 1:
            return None
    return divs

def solve(n, j):
    start = datetime.datetime.utcnow()
    b = 2**(n-1) + 1
    res = []
    for i in xrange(2**(n-3)):
        m = b + 2*i
        divs = fits(m)
        if not divs:
            continue
        now = datetime.datetime.utcnow()
        seconds = (now - start).total_seconds()
        print 'Found another number, now have %i, seconds passed: %r' % (len(res) + 1, seconds)
        res.append((m, divs))
        if len(res) == j:
            return res

if __name__ == "__main__":
    n = 32
    j = 500
    build_primes(2**(n/2 + 1))
    print 'Primes are built'
    res = solve(n, j)
    with open('C-large.out', 'w') as f:
        f.write('Case #1:\n')
        for num, divs in res:
            f.write('%s %s\n' % (bin(num)[2:], ' '.join(map(str, divs))))

