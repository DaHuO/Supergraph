#!/usr/bin/python
import sys
import math


def print_jcoins(case_nr, jcoin_dict):
    sys.stdout.write("Case #{}:\n".format(case_nr))
    for jc, divs in jcoin_dict.iteritems():
        divs = map(str, divs)
        divs = " ".join(divs)
        sys.stdout.write("{} {}\n".format(jc, divs))


def smallest_divisor(nr):
    if nr % 2 == 0:
        return 2

    div = 3
    r = math.sqrt(nr)
    while nr % div and div < r:
        div += 2
    if nr % div == 0:
        return div
    return 1


def jamcoin():
    cases = int(sys.stdin.readline().strip())
    assert cases == 1
    length, nr_coins = map(int, sys.stdin.readline().strip().split())
    
    coin_minstr = "1" + "0" * (length - 2) + "1"
    # Results
    results = {}  # number -> [div1, div2, div3, ...]
    
    curr = coin_minstr
    while len(results) < nr_coins:
        divs = []
        for base in xrange(2, 11):
            nr = int(curr, base=base)
            d = smallest_divisor(nr)
            if d != 1:
                divs.append(d)
            else:
                break
        if len(divs) == 9:
            results[curr] = divs
        curr = bin(int(curr, base=2) + 2)[2:]
    print_jcoins(1, results)


if __name__ == '__main__':
    jamcoin()

