#!/usr/bin/python3.4

import sys
import math
from functools import reduce

def solve(n, j):
    #test all jam coins
    nb_found = 0
    for i in range(2**(n - 2)):
        jc = '1' + bin(i)[2:].zfill(n-2) + '1'
        lst = []
        for base in range(2, 11):
            numb = int(jc, base)
            r = is_prime(numb)
            lst.append(r)
            if r == True:
                break

        if True not in lst:
            print(jc, ' '.join([str(i) for i in lst]))
            nb_found += 1

        if nb_found >= j:
            return

    return 0

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return True

def main():
    nb = int(get_line())
    for case_id in range(1, nb + 1):
        n, j = [int(i) for i in get_line().split(' ')]

        print('Case #%d:' %(case_id), file = o)
        ret = solve(n, j)

def get_line():
    return f.readline().strip()

def open_files():
    if len(sys.argv) == 1:
        f = sys.stdin
        o = sys.stdout

    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        o = sys.stdout

    if len(sys.argv) == 3:
        f = open(sys.argv[1], 'r')
        o = open(sys.argv[2], 'w')

    return (f, o)

if __name__ == "__main__":
    (f, o) = open_files()
    main()

