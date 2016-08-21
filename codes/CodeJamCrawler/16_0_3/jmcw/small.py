
import sys
import math

t = int(raw_input())

gfs = {}
gp = {}

def is_prime(n, b, p):
    for i in [2] + range(3, int(math.sqrt(n))+1, 2):
        if not i in gfs[b]: gfs[b][i] = i - (p % i)
        if n % i == gfs[b][i]: return i
    return -1

def find_factors(n):
    fs[2] = 2 - (n % 2)
    for i in range(3, int(math.sqrt(n))+1, 2):
        fs[i] = i - (n % i)
    return fs

def is_jamcoin(coin):
    factors = []
    for b in range(2,11):
        v = 0
        x = 1
        for i in range(len(coin)):
            if coin[-1-i] == 1:
                v += x
            x *= b
        x = is_prime(v, b, gp[b])
        if x == -1: return []
        factors += [x]
    return factors

def inc(coin):
    for i in range(len(coin)-2,-1,-1):
        if coin[i] == 0:
            coin[i] = 1
            return
        else:
            coin[i] = 0

for i in range(t):
    print "Case #{}:".format(i+1)

    n,j = [int(x) for x in raw_input().split(" ")]

    for b in range(2,11):
        gp[b] = b**(n-1)
        gfs[b] = {}

    jamcoin = [0 for x in range(n-2)] + [1]

    for a in range(j):
        res = is_jamcoin(jamcoin)
        while len(res) == 0:
            inc(jamcoin)
            res = is_jamcoin(jamcoin)
        sys.stdout.write("1")
        print "".join([str(x) for x in jamcoin]),
        print " ".join([str(x) for x in res])
        inc(jamcoin)
        sys.stdout.flush()
