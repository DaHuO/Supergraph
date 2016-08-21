DEBUG = 0
PRIMES = [2]
PRIME_SEARCHED = 2
def extend_PRIMES_upto(n):
    global PRIME_SEARCHED
    if DEBUG > 0:
        print 'extend_PRIMES_upto(%d)' % n
    if DEBUG > 1:
        print 'extending from', PRIMES[-1]+1, 'upto', n
    for i in xrange(PRIMES[-1]+1, n+1):
        for p in PRIMES:
            if i % p == 0:
                break
            if p * p > i:
                PRIMES.append(i)
                break
        else:
            PRIMES.append(i)
    if n > PRIME_SEARCHED:
        PRIME_SEARCHED = n


def divider(n):
    if DEBUG:
        print 'divider(%d)' % n
    global PRIME_SEARCHED
    if n <= PRIME_SEARCHED:
        if DEBUG:
            print 'n <= PRIME_SEARCHED:'
        if (n in PRIMES):
            return None
        else:
            for p in PRIMES:
                if n % p == 0:
                    return p
            else:
                assert False   
    elif n <= PRIME_SEARCHED * PRIME_SEARCHED:
        if DEBUG :
            print 'n <= PRIME_SEARCHED * PRIME_SEARCHED:'
        for p in PRIMES:
            if n % p == 0:
                return p
        else:
            return None
    else:
        import math
        if DEBUG :
            print 'extending to', int(math.ceil(math.sqrt(n)))
        extend_PRIMES_upto(int(math.ceil(math.sqrt(n))))
        assert n <= PRIME_SEARCHED * PRIME_SEARCHED
        return divider(n)

def solve(N, J):
    if DEBUG > 0:
        print 'solve(%s, %s, %s)' % (N, J, full)
    jamcoins = []
    for i in xrange(2**(N-2)):
        hoge = ('1{0:0%db}1' % (N-2)).format(i)
        dividers = []
        for base in range(2, 10+1):
            fuga = divider(int(hoge, base))
            if fuga:
                dividers.append(fuga)
            else:
                break
        else:
            if DEBUG > 0:
                print ' found', hoge
            yield (hoge, dividers)
            # jamcoins.append((hoge, dividers))
            # if len(jamcoins) >= J and not full:
            #     return jamcoins
    # if full:
    #     return jamcoins


def main():
    T = input()
    for i in range(T):
        N, J = map(int, raw_input().split())
        coins = solve(N, J)
        print 'Case #%d:' % (i+1)
        for jc, dividers in coins:
            print jc, ' '.join(map(str, dividers))
            if i+1 >= J:
                break

#
def main_(T, N, J, out):
    print 'main_(%s, %s, %s, %s)' % (T, N, J, out)
    coins = solve(N, J)
    print >>out, 'Case #%d:' % 1
    for i, (jc, dividers) in enumerate(coins):
        print >>out, jc, ' '.join(map(str, dividers))
        out.flush()
        print i
        if i+1 >= J:
            print 'broke'
            break


def solve_small():
    with open('C-small.out', 'w') as f:
        main_(1, 16, 50, f)
