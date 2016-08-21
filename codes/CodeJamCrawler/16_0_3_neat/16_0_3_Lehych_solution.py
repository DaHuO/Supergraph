#!/usr/bin/env python
import sys
from math import sqrt

def next_coin(coin_len):
    assert coin_len>=2
    tpl = "1%s1"
    i = 0
    for i in xrange(0, 2**(coin_len-2)):
        yield tpl % bin(i)[2:].rjust(coin_len-2, '0')

def divider(n):
    lim = int(sqrt(n))
    max_lim = 10000000
    for x in xrange(2, lim if lim < max_lim else max_lim):
        if n%x == 0:  # Non prime
            return x
    return None

def coin_in_bases(coin):
    return [int(coin, base) for base in range(2, 11)]

def main(testcase):
    coin_len, coins_count = map(int, testcase.split(' '))
    results = []
    for coin in next_coin(coin_len):
        coin_dividers = []
        for coin_repr_in_base in coin_in_bases(coin):
            d = divider(coin_repr_in_base)
            if d is None:
                break
            else:
                coin_dividers.append(d)
        assert len(coin_dividers)<10
        if len(coin_dividers)<9:
            continue
        results.append([coin] + coin_dividers)
        print ' '.join([str(y) for y in results[-1]])
        if len(results)>=coins_count:
            break

    return "\n" + "\n".join([' '.join([str(y) for y in x]) for x in results])

if __name__ == '__main__':
    cases_count = input()
    for i in xrange(1, cases_count+1):
        testcase = raw_input()
        if testcase == '':
            break
        # print "Case #%i: %s" % (i,  main(testcase.strip()))
        print "Case #%i:" % i
        main(testcase.strip())

