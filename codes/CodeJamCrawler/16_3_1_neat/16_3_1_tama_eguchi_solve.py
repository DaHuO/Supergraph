#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem A. Senate Evacuation
# https://code.google.com/codejam/contest/4314486/dashboard#s=p0
#

import sys
import random


def solve(Plist):
    Pmap = dict((chr(ord('A') + index), count) for index, count in enumerate(Plist))
    sortPlist = lambda: [party for party, count in sorted(Pmap.items(), key=lambda x: x[1], reverse=True)]
    countP = lambda: sum(Pmap.values())

    def decrementP(parties):
        for party in parties:
            Pmap[party] -= 1

    result = []

    if countP() % 2:
        party = sortPlist()[0]
        result.append(party)
        decrementP(party)

    while countP():
        parties = ''.join(sortPlist()[:2])
        result.append(parties)
        decrementP(parties)

    return ' '.join(result)


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        N = int(IN.readline().strip())
        Plist = map(int, IN.readline().strip().split())
        OUT.write('Case #{}: {}\n'.format(index + 1, solve(Plist)))


def makesample(T=100, maxN=26, sumP=1000):
    print(T)
    for n in range(T):
        N = random.randint(2, maxN)
        print(N)
        Plist = []
        for index in range(N):
            P = random.randint(1, sumP)
            Plist.append(P)
        print(' '.join(map(str, Plist)))


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)
