import sys
import string
digs = string.digits + string.letters

def int2base(x, base, l=0):
    if x < 0: sign = -1
    else: sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[x % base])
        x /= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    digits = ''.join(digits)
    if l:
        digits = '0'*(l-len(digits))+digits
    return digits

input = file(sys.argv[1])

primes = list()
def make_prime():
    N = 1 << 16
    s = [1] * N
    for i in range(2, N):
        if s[i]:
            primes.append(i)
            for j in range(i*2, N, i):
                s[j] = 0

def check(x):
    np = [0] * 12
    for b in range(2, 11):
        xx = 0
        for a in x:
            xx = xx * b + int(a)
        import math
        sqrt_xx = int(math.sqrt(xx+1))
        for p in primes:
            if p > sqrt_xx:
                return 0
            if xx % p == 0:
                np[b] = p
                break
    for p in np[2:11]:
        if not p:
            return 0
    print x, ' '.join(map(str, np[2:11]))
    return 1

def solve(n, k):
    for i in range(1<<29, 1<<(n-2)):
        x = '1' + int2base(i, 2, n-2) + '1'
        if check(x):
            k -= 1
        if not k:
            break

for case in range(int(input.readline())):
    make_prime()
    v = input.readline().split()
    print "Case #%d:" % (case+1)
    solve(int(v[0]),int(v[1]))
