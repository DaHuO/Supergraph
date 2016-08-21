from random import randint

def tobase(x,base):
    res, i = 0, 1
    while x>0:
        if x & 1 > 0:
            res += i
        x >>= 1
        i *= base
    return res

def is_pseudoprime(x):
    for div in range(2, min(x, 100)):
        if x % div == 0:
            return div
    return 0

def gen_jamcoin(N, J):
    S = set()
    while len(S) < (1 << (N - 2)):
        while True:
            inner = randint(0, (1 << (N - 2)) - 1)
            if inner not in S:
                S.add(inner)
                break
        x = (inner << 1) | 1 | (1 << (N - 1))
        divisors = []
        for base in range(2, 11):
            div = is_pseudoprime(tobase(x,base))
            if div == 0: break
            divisors.append(div)
        if len(divisors) == 9:
            yield [x] + divisors
            J -= 1
            if J == 0: return

T = int(input())

for t in range(T):
    print('Case #{}:'.format(t+1))
    N, J = [int(x) for x in input().split()]
    for jamcoin in gen_jamcoin(N, J):
        print(bin(jamcoin[0])[2:], end='')
        for div in jamcoin[1:]:
            print('', div, end='')
        print()
