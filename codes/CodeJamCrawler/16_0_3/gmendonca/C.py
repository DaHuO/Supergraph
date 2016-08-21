import numpy as np
import time


def is_prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def smallestdivisor(num):
    d = 2
    while num % d != 0:
        d = d + 1
    return d

def is_jamcoin(binary):
    list_divisor = []
    for i in range(2,11):
        num = int(''.join(str(v) for v in binary), i)
        if not is_prime(num):
            list_divisor.append(num/smallestdivisor(num))
        else:
            return (False, [])
    return (True, list_divisor)


t = int(raw_input().strip())
d = {}
for x in range(1,t+1):
    n,j= raw_input().split()
    print 'Case #%d:' % x
    for i in range(1,int(j)+1):
        binary = y = []
        z = False
        while not z:
            binary = np.random.choice([0, 1], size=int(n)-2, p=[0.5, 0.5])
            binary = [1] + list(binary)
            binary = binary + [1]
            if(d.has_key(''.join(str(v) for v in binary))):
                continue
            (z, y) = is_jamcoin(binary)
            d[''.join(str(v) for v in binary)] = True
        print ''.join(str(v) for v in binary),' '.join(str(u) for u in y)
