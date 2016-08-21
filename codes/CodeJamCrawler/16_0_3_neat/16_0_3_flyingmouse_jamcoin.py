import math

def isPrime(x):
    if x <= 1: return False, None
    if x == 2: return True, None
    if x % 2 == 0: return False, 2
    i=3
    while i * i <= x:
        if x % i == 0:
            return False, i
        i += 2
    return True, None

def isLegitimate(n):
    derives = []
    for i in xrange(2,11):
        val = 0
        for c in str(n):
            c = int(c)
            val = i * val + c
        flagPrime, derive = isPrime(val)
        if flagPrime:
            return False, None
        else:
            # print i, val
            derives.append(derive)
    return True, derives

def getCoins(n,m):
    maxLoop = int(math.pow(2, n-2))
    cnt = 0
    for i in xrange(maxLoop):
        zeros = '0' * (n - len(bin(i)))
        mid = zeros + bin(i)[2:]
        jamcoin = '1' + mid + '1'
        flagLegitimate, derives = isLegitimate(jamcoin)
        if flagLegitimate:
            cnt += 1
            div = ''.join(str(d)+' ' for d in derives)[:-1]
            print jamcoin, div
        if cnt == m:
            break



t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}:".format(i)
    getCoins(n, m)
