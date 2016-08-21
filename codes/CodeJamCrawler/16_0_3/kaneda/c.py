def y(func):
    return func(raw_input())


def Q(func):
    return map(func, raw_input().split())


def W(case, out, pattern='Case #%d: %s'):
    print pattern % (case, out)


def r(func, times):
    return[func()for _ in xrange(times)]
with open('primes.txt')as f:
    h = map(int, f.read().split())


def k(u):
    for p in h:
        if p < u and u % p == 0:
            return p
W(1, '')
T = y(int)
for t in xrange(1, T+1):
    N, J = Q(int)
    C = int('1%s1' % ('0'*(N-2)), 2)
    M = int('1'*N, 2)
    e = 0
    for x in xrange(C, M+1, 2):
        x = bin(x)[2:]
        R = []
        for P in xrange(2, 11):
            u = int(x, P)
            q = k(u)
            if not q:
                break
            R.append(q)
        else:
            assert len(R) == 9
            print x, ' '.join(map(str, R))
            e += 1
            if e == J:
                break
