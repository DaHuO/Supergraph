from itertools import product
from random import randrange
from math import sqrt
from time import time

dataset = "LARGE"
if dataset == "SMALL":
    N, J = 16, 50
elif dataset == "TEST":
    N, J = 6, 3
if dataset == "LARGE":
    N, J = 32, 500

lastTried = time()
skipped = False

# Miller-Rabin primality test
primesMemo = set()  # store found primes
small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 34, 47, 53, 59,
                61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
                131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191]

# some precalculated numbers
#print("preparing primes")
with open("primesList", "r+") as f:
    lines = f.readlines()
small_primes = [int(l.strip("\n").strip()) for l in lines]
#print("Primes prepared")

storedDivisors = {1326443518324400147398873: 1152846547}

def probably_prime(n, k):
    """Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite.
    """
    if n < 2: return False
    for p in small_primes:
        if n < p * p:
            return True
        if n % p == 0:
            return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# AKS Primality test
def expand_x_1(n):
    # This version uses a generator and thus less computations
    c =1
    for i in range(n//2+1):
        c = c*(n-i)/(i+1)
        yield c

def aks(p):
    if p==2:
        return True

    for i in expand_x_1(p):
        if i % p:
            # we stop without computing all possible solutions
            return False
    return True

def isCoinJam(n):
    for base in range(2, 11):
        bn = int(n, base)
        # check if it is prime
        if bn in primesMemo or  probably_prime(bn, 30):
        #print(bn, end = " ")
        #if aks(bn):
            #print(" is prime")
            return False
        #print(" is NOT prime")
    return True


def prove(coin):
    global skipped
    for base in range(2, 11):
        jam = int(coin, base)
        lb = 3
        hb = int(sqrt(jam))+2
        #print("\n>>>Proving: ", jam)
        if jam in storedDivisors.keys():
            print(storedDivisors[jam], end = " ")
            continue
        if jam % 2 == 0:
            print(2, end = " ")
            continue
        #for p in small_primes:
        #    if jam%p == 0:
        #        print(p, end = " ")
        #        continue
        for d in range(lb, hb, 2):
            #print(d)
            if jam%d == 0:
                print(d, end = " ")
                break
            if time()-lastTried > 30:
                skipped = True
                return


def generate(N, J):
    from random import choice
    global skipped, lastTried
    perms = ["0", "1"]
    middle = N-2
    for p in product(perms, repeat=middle):
        p = ''.join([choice(perms) for _ in range(middle)])  # now with random
        p = "1"+''.join(p)+"1"
        #if J == 1:
        #    p = "111001"
        #print("<>{0}<>".format(J))
        #print("<>{0}<>".format(p))
        if isCoinJam(p):
            print(p, end = " ")
            lastTried = time()
            prove(p)
            print()
            if skipped:
                #print("SKIPPED")
                skipped = False
            else:
                J -= 1

        #print("<>{0}<>".format(J))
        p = p[::-1]
        if isCoinJam(p):
            print(p, end = " ")
            lastTried = time()
            prove(p)
            print()
            if skipped:
                #print("SKIPPED")
                skipped = False
            else:
                J -= 1

            if J == 0:
                return


print("Case #1:")

generate(N, J)
