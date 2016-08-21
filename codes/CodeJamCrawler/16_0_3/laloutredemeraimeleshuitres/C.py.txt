primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

def t(i, N):
    s = format(i, 'b')
    return '1' + '0'*(N-2-len(s)) + s + '1'

def test_base(s, b):
    i = int(s, b)
    for p in primes:
        if i % p == 0:
            return p
    return 0

def test(s):
    L = [test_base(s, b) for b in range(2,11)]
    if all(L):
        return s, L
    return None

def test_N(N, target):
    L = []
    for i in range(2**(N-2)):
        r = test(t(i, N))
        if r:
            L.append(r)
        if len(L) == target:
            return L

