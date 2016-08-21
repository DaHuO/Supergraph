import sys
import StringIO

import random

# Deterministic Miller-Rabin
# from BjornEdstrom in Euler196

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def witness(b, n):
    # n - 1 == u * 2**t
    u = n - 1
    t = 0
    while not u & 1:
        u >>= 1
        t += 1
    
    x0 = pow(b, u, n)
    x1 = 0
    for i in xrange(1, t+1):
        x1 = pow(x0, 2, n)
        if x1 == 1 and x0 != 1 and x0 != (n - 1):
            return False
        if i == t and x1 != 1:
            return False
        x0 = x1
    return True

def is_prime(n):
    """is_prime(n) -> True if prime, False otherwise."""
    if n < 2:
        return False
    elif n == 2:
        return True
    elif not n & 1:
        return False
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False    
    if not witness(2, n): return False
    if not witness(7, n): return False
    if not witness(61, n): return False
    if n < 4759123141L:
        return True
    if not witness(3, n): return False
    if not witness(24251, n): return False
    elif n < 10000000000000000L:
        if n == 46856248255981L: # is this the only false or the smallest?
            return False
        return True
    #raise ValueError, "n too large atm."
    for x in range(randint(5, 10)):
        if not witness(randint(1, n - 1), n):
            return False
    return True # probable

factors = filter(is_prime, xrange(1000000))

def return_factor(n):
    for f in factors:
        if f >= n:
            return -1
        if n % f == 0:
            return f
    return -1

def random_jamcoin(N):
    return '1' + ''.join(random.choice('01') for i in xrange(N-2)) + '1'

def jamcoin_ff(s):
    ff = []
    for base in xrange(2, 11):
        n = int(s, base)
        f = return_factor(n)
        if f<0:
            return False
        ff.append(f)
    return ff


def doit(N, J):
    i = 0
    jcs = set()
    while i < J:
        jc = random_jamcoin(N)
        ff = jamcoin_ff(jc)
        if ff and jc not in jcs:
            i += 1
            jcs.add(jc)
            print jc, " ".join(map(str, ff))

sample = """1
6 3
"""

small = """1
16 50
"""

large = """1
32 500
"""

def stripnl(s):
    if s[-1]=="\n":
        return s[:-1]
    return s

def main(data = None):
    if data is None:
        f = sys.stdin
    else:
        f = StringIO.StringIO(data)
    nt = int(f.readline())
    for tc in xrange(nt):
        S = stripnl(f.readline())
        N, J = map(int, S.split(" "))
        print "Case #%d:" % (tc+1)
        doit(N, J)

main()
