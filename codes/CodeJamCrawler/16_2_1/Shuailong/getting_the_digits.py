#!/usr/bin/env python
# encoding: utf-8

"""
getting_the_digits.py

Created by Shuailong on 2016-05-01.

https://code.google.com/codejam/contest/11254486/dashboard

"""

from collections import Counter

def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        S = raw_input()
        res = ''
        cs = Counter(S)
        count = [0]*10
        count[0] = cs['Z']
        cs['E'] -= count[0]
        cs['R'] -= count[0]
        cs['O'] -= count[0]
        cs['Z'] -= count[0]

        count[2] = cs['W']
        cs['T'] -= count[2]
        cs['O'] -= count[2]
        cs['W'] -= count[2]

        count[4] = cs['U']
        cs['F'] -= count[4]
        cs['O'] -= count[4]
        cs['R'] -= count[4]
        cs['U'] -= count[4]

        count[5] = cs['F']
        cs['I'] -= count[5]
        cs['V'] -= count[5]
        cs['E'] -= count[5]
        cs['F'] -= count[5]

        count[6] = cs['X']
        cs['S'] -= count[6]
        cs['I'] -= count[6]
        cs['X'] -= count[6]

        count[7] = cs['V']
        cs['S'] -= count[7]
        cs['E'] -= 2*count[7]
        cs['N'] -= count[7]
        cs['V'] -= count[7]

        count[8] = cs['G']
        cs['E'] -= count[8]
        cs['I'] -= count[8]
        cs['H'] -= count[8]
        cs['T'] -= count[8]
        cs['G'] -= count[8]

        count[9] = cs['I']
        cs['N'] -= 2*count[9]
        cs['E'] -= count[9]
        cs['I'] -= count[9]

        count[3] = cs['R']
        cs['T'] -= count[3]
        cs['H'] -= count[3]
        cs['R'] -= count[3]
        cs['E'] -= 2*count[3]

        count[1] = cs['O']
        cs['O'] -= count[1]
        cs['N'] -= count[1]
        cs['E'] -= count[1]

        for i in cs:
            if cs[i]:
                print 'HAHAHA:', i

        for digit in range(len(count)):
            for i in range(count[digit]):
                res += str(digit)

        print 'Case #{}: {}'.format(t, res)


if __name__ == '__main__':
    main()
