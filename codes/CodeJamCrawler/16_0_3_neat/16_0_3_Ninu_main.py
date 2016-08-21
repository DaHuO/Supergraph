import random
import sys


def extract(nr, b):
    res = 0
    while nr > 0:
        res = res * b + (nr % 2)
        nr = nr // 2
    return res


def getSmallestDiv(tmp):
    if tmp % 2 == 0:
        return 2
    d = 3
    while d * d <= tmp and d < 100:
        if (tmp % d == 0):
            return d
        d = d + 2
    return 1


def toString(nr):
    s = ''
    while nr > 0:
        if nr % 2 == 0:
            s = s + '0';
        else:
            s = s + '1'
        nr = nr // 2
    return s


def solve(n, j):
    f = open('output.txt', 'w')
    f.write('Case #1:\n')
    dictionar = dict()
    random.seed()
    while len(dictionar.keys()) < j:
        tmp = random.randint(0, 2 ** (n - 2))
        for i in range(max(0,tmp - 100), min(tmp + 100, 2 ** (n - 2))):
            nr = ((1 << (n - 1)) | (i << 1) | 1)
            v = []
            for b in range(2, 11):
                tmp = extract(nr, b)
                div = getSmallestDiv(tmp)
                if div == 1:
                    break
                else:
                    v.append(div)
            if len(v) == 9 and (nr in dictionar) == False:
                dictionar[nr] = True
                tmpStr = toString(nr)
                for k in range(0, 9):
                    tmpStr = tmpStr + ' '
                    tmpStr = tmpStr + str(v[k])
                tmpStr = tmpStr + '\n'
                f.write(tmpStr)
                f.flush()
                if len(dictionar.keys()) == j:
                    break;
    f.close()

solve(32, 500)
