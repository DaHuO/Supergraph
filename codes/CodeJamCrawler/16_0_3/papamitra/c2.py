#!/usr/bin/env python3

import sys
import math

def divisor(jc, base):
    n = int(jc, base)
    for i in range(2,20):
        if (n % i) == 0: return i
    raise Exception('prime', 'prime')

def solve(n,j):
    for i in range(int('1'*(n-2),2)+1):
        jamcoin = '1' + format(i, '0{0}b'.format(n-2)) + '1'
        try:
            print(jamcoin, *[str(divisor(jamcoin, d)) for d in range(2,11)])
            j -= 1
            if j==0: break
        except:
            pass

def main():
    sys.stdin.readline()
    for i,l in enumerate(sys.stdin.readlines()):
        (n, j) = [int(x) for x in l[:-1].split(' ')]
        print("Case #{0}:".format(i+1))
        solve(n, j)

if __name__ == '__main__':
    main()
