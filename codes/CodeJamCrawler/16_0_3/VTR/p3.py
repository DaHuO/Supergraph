__author__ = 'VTR'
import random


def toBase(s, x):
    res = 0
    c = 1
    for i in range(len(s)-1, -1, -1):
        res += c * (ord(s[i]) - 48)
        c *= x
    return res


def isPrime(n):
    i = 2
    mxTests = 0
    while i * i <= n:
        if n % i == 0:
            return i, False
        i += 1
        if i > 50000:
            return n, True
    return n, True


def printBase(n, x):
    if n == 0:
        return ''
    else:
        return printBase(n / x, x) + chr(n % x + 48)


def isOk(n):
    d = []
    for i in range(2, 11):
        last = isPrime(toBase(n, i))
        if last[1] is True:
            return None
        d.append(str(last[0]))
    return d


def get_random(x):
    s = ''
    for i in range(x):
        if random.randint(0, 1) == 0:
            s += '0'
        else:
            s += '1'
    return s

j = 500
chosed = {}
fp = open('log', 'w')
fp.write('Case #1:\n')
while j > 0:
    s = '1' + get_random(30) + '1'
    if s in chosed:
        continue
    else:
        chosed[s] = 1
    if toBase(s, 10) % 2:
        r = isOk(s)
        if r is not None:
            fp.write(s + ' ' + ' '.join(r) + '\n')
            j -= 1
            print 'mai am ', j
fp.close()