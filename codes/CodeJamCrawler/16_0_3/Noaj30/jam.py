# Google Code Jam Qualification Round 2016
# Problem C. Coin Jam

from math import sqrt

def prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False, str(i)
    return True, 0

def base(N, b, L):
    s = 0
    r = N[::-1]
    for i in range(L):
        s += (b**i)*int(r[i])
    return s

def update(x, N):
    y = [i for i in x[1:-1][::-1]]
    for i in range(N - 2):
        if y[i] == '1':
            y[i] = '0'
        else:
            y[i] = '1'
            z = '1'
            for j in y[::-1]:
                z += j
            return z + '1'

def create(N, J):
    x = '1' + (N - 1)*'0'
    coins = []
    while len(coins) < J:
        x = update(x, N)
        good = True
        proof = [x]
        for i in range(2, 11):
            k = prime(base(x, i, N))
            if k[0]:
                good = False
                break
            else:
                proof += [k[1]]
        if good:
            coins += [proof]
            print len(coins)
    return coins

def small():
    g = open('small.txt', 'w')
    g.write('Case #1:' + '\n')
    line = 1
    for i in create(16, 50):
        for j in i[:-1]:
            g.write(j + ' ')
        g.write(i[-1] + (line != 50)*'\n')
        line += 1
    g.close()
