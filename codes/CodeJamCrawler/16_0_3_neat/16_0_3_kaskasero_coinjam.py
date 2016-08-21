# Code Jam 2016
# Raoul Veroy
import fileinput
from math import sqrt

stdin = fileinput.input()

def gen_primes( num ):
    flags = [ True ] * (num+1)
    flags[0] = False
    flags[1] = False
    count = 0
    for x in xrange(2, int(sqrt(num)) + 1):
        if flags[x]:
            y = x * x
            while y <= num:
                flags[y] = False
                y = y + x
    return [ x for x in xrange(2,len(flags)) if flags[x] ]

primes = gen_primes(65535)

primeset = set(primes)

def get_next( coin = "" ):
    tmp = int(coin, 2)
    tmp += 1
    while tmp % 2 != 1:
        tmp += 1
    return "{0:b}".format(tmp)

def get_divisor( num = 0 ):
    if num < 2:
        return 0
    if num < primes[-1] and num in primes:
        return 0
    for p in primes:
        if p > num:
            assert(False)
        if num % p == 0:
            return p
    return 0

def coin_jam_proof( cand = "" ):
    proof = []
    for base in range(2, 11):
        d = get_divisor( int(cand, base) )
        if d == 0:
            return []
        proof.append(d)
    return proof
results = {}
count = int(stdin.next())
assert(count == 1)
print "Case #%d:" % count
line = stdin.next().rstrip()
N, J = line.split(" ")
width = int(N)
cjams = int(J)
start = "1" + ("0" * (width - 2)) + "1"
end = "1" * width
cur = start
expected = int(end, 2) - int(start, 2) + 1
total = 0
done = 0
while ( (total < cjams) and
        (done < expected) and 
        (cur != end) ):
    cur = get_next(cur)
    proof = coin_jam_proof( cur )
    if len(proof) > 0:
        assert(len(proof) == 9)
        print cur,
        for x in proof:
            print x,
        print
        total += 1
    done += 1
