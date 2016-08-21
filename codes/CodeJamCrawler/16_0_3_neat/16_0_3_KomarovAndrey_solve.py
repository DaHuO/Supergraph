from sympy import ntheory
from random import *
from sys import stdout

def check(coin):
    if ntheory.isprime(coin):
        return None
    d = []
    for radix in range(2, 11):
        div = ntheory.factorint(int(coin, radix))
        if len(div) >= 2:
            d.append(list(div)[0])
        else:
            return None
    return d

randcoin = lambda n : '1' + ''.join(choice('01') for i in range(n - 2)) + '1'

n = 32
k = 500
it = 0
good = set()

print('Case #1:')
while True:
    c = randcoin(n)
    d = check(c)
    if d and c not in good:
        print('{} {}'.format(c, ' '.join(map(str, d))))
        stdout.flush()
        it += 1
        good.add(c)
        if it == k:
            break
