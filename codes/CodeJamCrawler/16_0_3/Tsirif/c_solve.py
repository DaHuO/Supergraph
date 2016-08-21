#!/usr/bin/env python
# encoding: utf-8

"""
Submission for problem C: Coin Jam
of Google CodeJam 2016

Author: Tsirigotis Christos <tsirif@gmail.com>
Date: April 09, 2016
"""

import itertools
from fractions import gcd

OUTPUT = "Case #%(nc)s:"
def print_jamcoin(jc, p):
    output = str(jc)
    for i in p:
        output += " "+str(i)
    print(output)

T = 1
N = 32
J = 500
MAX_TURNS = 10
JAMCOINS = []
PROOFS = []

def solve():
    T = int(raw_input()) # 1 <= T <= 100
    for nc in xrange(1, T+1):
        print(OUTPUT % locals())
        N, J = map(int, raw_input().split())
        j = 0
        for a in itertools.product(['0', '1'], repeat=N-2):
            jc = "".join(['1'] + list(a) + ['1'])
            is_jamcoin = True
            p = []
            for base in xrange(2, 11):
                test_jc = int(jc, base)

                """
                Implement a Pollard's rho algorithm with iteration window
                """
                turns = 0
                x_fixed = 2
                cycle_size = 2
                x = 2
                factor = 1
                while factor == 1:
                    count = 1
                    while factor <= 1 and count <= cycle_size:
                        x = (x**2 + 1) % test_jc
                        factor = gcd(x - x_fixed, test_jc)
                        count += 1
                        turns += 1
                        if turns >= MAX_TURNS:
                            is_jamcoin = False
                            break
                    if not is_jamcoin:
                        break
                    cycle_size *= 2
                    x_fixed = x
                if not is_jamcoin:
                    break
                if factor == test_jc:
                    is_jamcoin = False
                    break
                p.append(factor)

                #  divisor_found = False
                #  if test_jc % 2 == 0:
                #      p.append(2)
                #      divisor_found = True
                #      continue
                #  for i in xrange(3, int(test_jc**0.5)/3+1, 2):
                #      if test_jc % i == 0:
                #          p.append(i)
                #          divisor_found = True
                #          break
                #  if not divisor_found:
                #      is_jamcoin = False
                #      break

            if not is_jamcoin:
                continue
            j += 1
            print_jamcoin(int(jc), p)
            #  print(turns)
            JAMCOINS.append(int(jc))
            PROOFS.append(p)
            if j >= J:
                break

def test():
    for i in xrange(min([J, len(JAMCOINS)])):
        a = JAMCOINS[i]
        proof = PROOFS[i]
        if set(map(int, list(str(a)))) - set([0, 1]):
            return str(i) + ' 0/1 only FAIL'
        if str(a)[0] != '1' or str(a)[-1] != '1':
            return str(i) + ' 1xxx1 FAIL'
        for j in xrange(2, 11):
            if int(str(a), j) % proof[j-2] != 0:
                return str(i) + ' base' + str(j) + ' proof FAIL'
    return 'SUCCESS: found ' + str(len(JAMCOINS))

solve()
#  print(test())

