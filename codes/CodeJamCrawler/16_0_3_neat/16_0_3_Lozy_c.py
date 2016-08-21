from primesieve import *
isL = True
L = 500 if isL else 50
N = 16
k = 0
lst = generate_primes(10 ** 9)
cnt = 0
def check(n):
    ot = list()
    for i in xrange(2, 11):
        x = 0
        for j in xrange(0, N):
            if not (n & (1 << j)) == 0:
                x += i ** j
        fl = False
        for pr in lst:
            p = int(pr)
            if p * p >= x: break
            if x % p == 0:
                ot.append(int(p))
                fl = True
                break
        if not fl:
            return False, ot
    return True, ot
print "Case #1:"
while cnt < L and k < (1 << (N - 2)):
    x = (k << 1) | (1 << (N - 1)) | 1
    ok, ot = check(x)
    if ok:
        cnt += 1
        if isL: print bin(x)[2:]+bin(x)[2:], ' '.join(map(str, ot))
        else: print bin(x)[2:], ' '.join(map(str, ot))
    k += 1
