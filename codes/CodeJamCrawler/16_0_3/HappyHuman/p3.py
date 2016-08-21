import math
primes = {2: 0, 3: 0, 5: 0}

def is_prime(n):
    if n in primes:
        return primes[n]
    for i in range(3, int(math.sqrt(n)+1), 2):
        if n % i == 0:
            primes[n] = i
            return i
    primes[n] = 0
    return 0

def convert_base(sn, bas):
    r = 0
    i = 0
    for l in reversed(sn):
        if l == '1':
            r += (bas ** i)
        i += 1
    return r

def convert2bin(n):
    digits = []
    while n > 0:
        digits.insert(0, str(n&1))
        n = n >> 1
    return ''.join(digits)

def is_jamcoin(nstr):
    items = []
    for b in range(2, 11):
        nb = convert_base(nstr, b)
        x = is_prime(nb)
        if x == 0:
            return None
        else:
            items.append(x)
    return items
    

for i in xrange(int(raw_input().strip())):
    print "Case #%s:"%(i+1, )
    N, J = map(int, raw_input().strip().split(' '))
    n = int('1' + ''.join(['0'] * (N-2)) + '1', 2)
    k = 0
    while k < J:
        nstr = convert2bin(n)
        items = is_jamcoin(nstr)
        if items is not None:
            k += 1
            print nstr, ' '.join(map(str, items))
        n += 2
