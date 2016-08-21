import math
n = int(math.sqrt(1111111111111111))
sieve = [True] * max(2,n)
sieve[0], sieve[1]=False, False
for i in xrange(3,int(n**0.5)+1,2):
    if sieve[i]:
        sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
primes = [2] + [i for i in xrange(3, n, 2)]

def getDivisor(n):
    upper = int(math.sqrt(n))
    for item in primes:
        if item > upper:
            return -1
        if n%item == 0:
            return item

def getBaseNum(n, base):
    exp = 1
    res = 0
    while n>0:
        res += exp*(n&1)
        exp *= base
        n = (n>>1)
    return res

t = int(raw_input())
N, J = map(int, raw_input().split(' '))
lower = (1<<(N-2))
upper = 1<<(N-1)
print 'Case #1:'
for raw in xrange(lower,upper):
    cur = (raw<<1) + 1
    res = []
    for base in xrange(2,11):
        tmp = getBaseNum(cur,base)
        divisor = getDivisor(tmp)
        if divisor <= 0:
            break
        else:
            res.append(divisor)
    if len(res) == 9:
        tmplst = []
        while cur > 0:
            tmplst.append((cur&1))
            cur = (cur>>1)
        curNum = ''.join(map(str, tmplst[::-1]))
        print curNum, ' '.join(map(str, res))
        J -=1
    if J<=0:
        break






