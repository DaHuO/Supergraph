# Zolmeister

import sys
import random

fout = open(sys.argv[0] + '.out', 'w')
out = 'Case #1:'
print out
fout.write(out + '\n')

def isprime(n):
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2

    while i * i <= n:
        if i > 1000:
            return 1
        if n % i == 0:
            return i

        i += w
        w = 6 - w

    return 1


T = int(input())

def is_coin(coin):
    if coin[0] != '1' or coin[-1] != '1':
        return False

    divs = []
    for base in xrange(2, 11):
        div = isprime(int(coin, base))
        if div == 1:
            return False
        divs.append(div)

    return divs

# print is_coin('110011')

for t in xrange(T):
    [N, J] = map(int, raw_input().split(' '))
    # print N, J
    total = 0
    used = set()

    while True:
        rand = 0
        while rand % 2 != 1:
            rand = random.randint(2 ** (N - 1), 2 ** N)

        guess = str(bin(rand))[2:]
        # print guess
        divs = is_coin(guess)
        if divs != False and guess not in used:
            used.add(guess)
            total += 1
            ans = guess + ' ' + ' '.join(map(str, divs))
            print ans
            fout.write(ans + '\n')

        if total >= J:
            break



fout.close()
