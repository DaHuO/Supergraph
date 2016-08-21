def get_primes(limit):
    sqrtlim = int(limit**0.5)
    primes = set(range(3, sqrtlim + 1, 2))
    last = 3
    for i in range(3, sqrtlim+1, 2):
        if i in primes:
            last = i
            for j in range(i*i, sqrtlim + 1, i):
                primes.discard(j)

    more = sqrtlim + (sqrtlim % 2) + 1
    more_primes = set(range(more, limit + 1, 2))
    for p in primes:
        if (more % p == 0):
            start = more
        else:
            start = (more//p + 1) * p
            start += (1 - start % 2) * p
        for j in range(start, limit + 1, p):
            more_primes.discard(j)

    primes.add(2)
    primes.update(more_primes)
    #primelist = sorted(primes)
    return primes#, primelist


def to_base(num, b):
    o = []
    while num > 0:
        num, r = divmod(num, b)
        o.append(r)
    o.reverse()
    return int(''.join(str(n) for n in o))

def check(num, primes, primelist):
    factors = []
    for base in range(2, 11):
        n = int(num, base)
        if n in primes:
            return
        lim = int(n**0.5) + 1
        for p in primelist:
            if n % p == 0:
                factors.append(p)
                break
            if p > lim:
                return
        else:
            return

    return factors

if __name__ == '__main__':
    #SMALL
    maxprime = 33333334
    primes = get_primes(maxprime)
    primelist = sorted(primes)

    T = int(input())
    N, J = map(int, input().split())

    coin = (1 << (N-1)) + 1
    maxcoin = 1 << N

    print('Case #1:')
    found = 0
    while found < J and coin < maxcoin:
        cstr = bin(coin)[2:]
        factors = check(cstr, primes, primelist)
        if factors is not None:
            print(cstr, ' '.join(str(f) for f in factors))
            found += 1

        coin += 2

