# coding: utf-8
import random

BASELIST = [[(k+2)**i for i in range(32)] for k in range(9)]
JamCount = 0

def makeCoin(N):
    Coin = [0 for i in range(N)]
    Coin[0] = 1
    Coin[N-1] = 1
    
    KK = [random.randrange(2) for i in range(N-2)]
    for i in xrange(1,N-1):
        Coin[i] = KK[i-1]
    
    return Coin

def prime(q):
    q = abs(q)

    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1

    for i in xrange(50):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)

        while t != q-1 and y != 1 and y != q-1:
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

def makeBase(Coin,N):
    ret = [0 for i in range(9)]
    for i in range(9):
        for k in range(N):
            if Coin[(N-1)-k] == 1:
                ret[i] += BASELIST[i][k]
    return ret

def Base_is_ok(base):
    t = 1;
    for i in range(9):
        if prime(base[i]) == True:
            t = 0
            break
    return t == 1

def JamCoin(Coin):
    for i in range(9):
        if Coin[i]%2 == 0:
            Coin[i] = 2
            continue
        if Coin[i]%3 == 0:
            Coin[i] = 3
            continue
        for s in xrange(1,10002):
            if Coin[i]%(6*s-1) == 0:
                Coin[i] = (6*s-1)
                break
            if Coin[i]%(6*s+1) == 0:
                Coin[i] = (6*s+1)
                break
            if s == 10001:
                return False
    return Coin

def coinstr(c,N):
    s = ''
    for i in range(N):
        s += str(c[i])
    return s

def coinstr2(Coin):
    s = str(Coin[0])
    for i in xrange(1,9):
        s += ' ' + str(Coin[i])
    return s

T = input()
N,J = map(int,raw_input().split())
check = []
print 'Case #1:'
while JamCount < J:
    c = makeCoin(N)
    flag = 0
    for tt in check:
        if tt == c:
            flag = 1
            break
    if flag == 1:
        continue
    check.append(c)
    Coin = makeBase(c,N)
    if Base_is_ok(Coin) == True:
        if JamCoin(Coin) != False:
            Coin = JamCoin(Coin)
            JamCount += 1
            print coinstr(c,N),coinstr2(Coin)

