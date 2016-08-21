#!/usr/bin/env python3

from itertools import product
import sys

from numpy import float64   # so that float64(1)/0 == inf (avoid errors)
inf = float('inf')
read_ints = lambda : list(map(int, input().split()))

def brute(N, J):
    for p in product('01',repeat=N-2):
        p = '1' + ''.join(p) + '1'
        print('p= %s J=%d' % (p, J), file=sys.stderr)

        divs = [divisor(int(p, base=i)) for i in range(2,11)]
        if(all(divs)):
            J -= 1
            print(p, end=' ')
            for d in divs:
                print(d, end=' ')
            print('')
        if J == 0:
            break

def divisor(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return i
        i+=1
    return None

if __name__ == '__main__':
    T = input()
    N, J = read_ints()
    print('Case #1:')
    brute(N, J)