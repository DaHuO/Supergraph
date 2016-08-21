import math
import random

MAX_T = int(1e9)

# small
#N = 16
#J = 50
# large
N = 32
J = 500

def find_small_nontrivial_divisor(n):
    threshold = min(MAX_T, n)
    d = 2
    while d*d <= threshold:
        if n % d == 0:
            return d
        d += 1
    return None

def interpret_10(v, base):
    ans = 0
    p = 1
    for d in reversed(v):
        if d: ans += p
        p *= base
    return ans

def try_random_sequence():
    v = [False] * N
    for i in range(N):
        v[i] = random.choice([True,False])
    v[0] = v[N-1] = True

    divs = []
    for b in range(2,11):
        n = interpret_10(v, b)
        d = find_small_nontrivial_divisor(n)
        if not d:
            return None
        divs.append(d)
    return (interpret_10(v,10),divs)

def solve():
    print 'Case #1:'
    coins = []
    while len(coins) < J:
        coin = try_random_sequence()
        if coin:
            (n,divs) = coin
            if n in coins:
                continue
            print n,
            for d in divs:
                print d,
            print
            coins.append(n)

solve()

