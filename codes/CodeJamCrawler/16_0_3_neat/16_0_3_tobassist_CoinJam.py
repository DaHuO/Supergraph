from math import pow
from math import sqrt

from random import getrandbits
def string2dec(bits,base):
    dec = 0
    for i in range(len(bits)):
        dec = dec + (int(bits[-(i+1)]) * pow(base,i))
    return dec

def nonTrivialDivisors(n):
    i = 2
    while ((i) <= sqrt(n)):
        if n%i == 0:
            return i
        if i == 2:
            i = 3
        else:
            i = i + 2

def validate(coin):
    reps = []
    ntds = []
    for i in range(2,11):
        reps.append(int(string2dec(coin,i)))
        ntds.append(nonTrivialDivisors(reps[i-2]))
    if all(ntds) and int(coin[0]) and int(coin[-1]):
        return ntds
    else:
        return 0

def generateCoin(CoinLength,previousCoin):
    valid = 0;
    fmt_str = '0'+str(CoinLength-2)+'b'
    if not(previousCoin):
        coinMiddle_d = -1;
    else:
        coinMiddle_d = int(previousCoin[0][1:-1],2)
    while(not(valid)):
        coinMiddle_d = coinMiddle_d + 1
        coinMiddle_b = format(coinMiddle_d,fmt_str)
        coin = '1'+str(coinMiddle_b)+'1'
        valid = validate(str(coin))
    return [str(coin), valid]

def generateCoins(N,J):
    # Generate J N-bit coins
    coins = ['']*J
    coins[0] = generateCoin(N,0)
    for i in range(1,J):
        coins[i] = generateCoin(N,coins[i-1])
    return coins

f= open('C-small-attempt2.in','r')
# Read number of trials (T)
T = f.readline()
for t in range(int(T)):
    line = f.readline()
    N, J = line.split()
    coins = generateCoins(int(N),int(J))
    print 'Case #' + str(t+1) +':'
    for coin in coins:
        output = coin[0]
        for ntd in coin[1]:
            output = output + ' ' + str(ntd)
        print output
