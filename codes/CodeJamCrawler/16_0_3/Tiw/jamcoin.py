__author__ = 'chonnakan'


import time


def gen_coin(n):
    l = []
    nm = n-2

    for i in range(0, 2**nm):
        mm = '%s'%(bin(i)[2:].zfill(nm))
        #print mm
        l.append('1' + mm + '1')

    return l


def find_div(n):
    import math
    is_prime = True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return i
    if is_prime:
        return -1


def solve(n, j):
    coins = gen_coin(n)
    #print coins
    count = 0
    for coin in coins:
        ans = []
        for i in range(2, 11):
            #print int(coin, i)
            dd = find_div(int(coin, i))
            #print dd
            if dd == -1:
                break
            else:
                ans.append(dd)
        #print ans
        if len(ans) == 9:
            print coin,
            for a in ans:
                print a,
            print ''
            #print count
            count += 1
        if count == j:
            break
        #print '*'*100

s = time.time()
f = open('sample_jamcoin.txt')
cases = int(f.readline())

for c in range(1, cases+1):
    l = f.readline()
    n = int(l.split(' ')[0])
    j = int(l.split(' ')[1])
    print 'Case #%d' % c
    solve(n, j)
e = time.time()

print e-s
