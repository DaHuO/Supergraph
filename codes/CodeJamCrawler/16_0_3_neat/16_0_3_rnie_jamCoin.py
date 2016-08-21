import random

def toBase(coin, base, n):
    sum = base**(n-1) + 1
    revCoin = coin[::-1]
    for i, digit in enumerate(revCoin):
        sum += int(digit) * base**(i+1)
    return sum

def getCoin(seenCoins, n):
    coin = '{0:b}'.format(random.randint(0, 2**(n-2)-1))
    while coin in seenCoins:
        coin = '{0:b}'.format(random.randint(0, 2**(n-2)-1))
    seenCoins.append(coin)
    return str(coin.zfill(n-2))

def isValidCoin(coin, n):
    divisors = [3, 5, 7, 11, 13]
    for base in range(2,11):
        for div in divisors:
            val = toBase(coin, base, n)
            if val % div == 0:
                break
            elif div == 13:
                return False
    return True

def getCoinDivisors(coin, n):
    divisors = [3, 5, 7, 11, 13]
    coinDivisors = []
    for base in range(2,11):
        for div in divisors:
            if toBase(coin, base, n) % div == 0:
                coinDivisors.append(str(div))
                break
    return coinDivisors

t = int(raw_input())
n, j = [int(s) for s in raw_input().split(' ')]
seenCoins = []
validCoins = []

print 'Case #{}:'.format(t)
while len(validCoins) != j:
    coin = getCoin(seenCoins, n)
    while not isValidCoin(coin, n):
        coin = getCoin(seenCoins, n)
    # convert n-2 digit coin to n digit coin
    fullCoin = str(int(coin)*10 + 10**(n-1) + 1)
    validCoins.append([fullCoin] + getCoinDivisors(coin, n))
    
for c in validCoins:
    print ' '.join(c)
