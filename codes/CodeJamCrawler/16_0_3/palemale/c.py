import os, sys, itertools

def binseq(k):
    return [''.join(x) for x in itertools.product('01', repeat=k)]

def is_prime(n):
    if n == 2 or n == 3: return True, None
    if n < 2 or n%2 == 0: return False, 2
    if n < 9: return True, None
    if n%3 == 0: return False, 3
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False, f
        if n%(f+2) == 0: return False, f+2
        f +=6
    return True, None
    
def get_divisor(n, base):
    divisor = 2
    result = None
    dammit = int(n, base)
    while not result:
        if dammit % divisor == 0:
            result = divisor
    return divisor
    
def list_divisors(n):
    divisors = []
    for x in xrange(2, 11):
        divisors.append(get_divisor(n , x))
    return divisors

with open(sys.argv[1], 'r') as infile:
    N = int(infile.readline().strip())
    for x in xrange(1, N+1):
        N, J = map(int, infile.readline().strip().split())
        jams = {}
        for x in itertools.product('01', repeat=N):
            if x[0] != '1' or x[-1] != '1':
                continue
            result = ''.join(x)
            if result in jams:
                continue
            fail = False
            divisors = []
            for base in xrange(2, 11):
                int_res = int(result, base)
                prime, divisor = is_prime(int_res)
                if prime:
                    fail = True
                    break
                divisors.append(divisor)
            if not fail:
                jams[result] = divisors
            if len(jams) == J:
                break
        for jam, divisors in jams.iteritems():
            print jam, ' '.join([str(d) for d in divisors])