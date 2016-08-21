#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem D. Fractiles
# https://code.google.com/codejam/contest/6254486/dashboard#s=p3
#

import sys
import random


def solve(K, C, S):
    # 1回cleanするとCヶ所のGの有無がわかる
    # S回cleanできるので最大C*Sヶ所のGの有無がわかる
    # Kがそれより多いと判別できない
    if K > C * S:
        return 'IMPOSSIBLE'

    checkpos = range(K)
    clean = []
    while checkpos:
        cleanpos = 0
        for c in range(C):
            cleanpos += (K ** c) * checkpos.pop(0)
            if not checkpos:
                break
        clean.append(min(cleanpos + 1, K ** C))  # 1 origin
    return ' '.join(map(str, sorted(clean)))


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        K, C, S = map(int, IN.readline().strip().split())
        OUT.write('Case #{}: {}\n'.format(index + 1, solve(K, C, S)))


def makesample(T=100, Kmax=100, Cmax=100):
    print T
    for index in range(T):
        K = random.randint(1, Kmax)
        C = random.randint(1, Cmax)
        S = random.randint(1, K)
        while K ** C > 10 ** 18:
            C = random.randint(1, Cmax)
        print '{} {} {}'.format(K, C, S)


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)
