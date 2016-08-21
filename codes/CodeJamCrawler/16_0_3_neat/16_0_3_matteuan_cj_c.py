from itertools import product

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])

def find_divisor(x):
    for i in _known_primes:
        if x % i == 0:
            return i
    return -1

def solve(N, J):
    sol = []
    a = product(['0','1'], repeat=(N-2))
    for i in range(J):
       
        for j in range(N*100000):
            if j % 10 == 0:
                print(j)
            b = "1" + "".join(a.__next__()) + "1"
            numbers = [int(b, k) for k in range(2,11)]
            if any(map(is_prime, numbers)):
                continue
            divisors = list(map(find_divisor, numbers))
            if -1 in divisors:
                continue
            sol.append("{} {} {} {} {} {} {} {} {} {}".format(b, *divisors))
            break
    print("arriato")
    return "\n".join(sol)

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 5000, 2) if is_prime(x)]
nf = input()
out = nf + ".out"
fout = open(out, 'w')
f = open(nf)
T = int(f.readline())
NJ = f.readline().split(" ")
N = int(NJ[0])
J = int(NJ[1])
fout.write('Case #1:\n{}\n'.format(solve(N, J)))
fout.close()
f.close()
