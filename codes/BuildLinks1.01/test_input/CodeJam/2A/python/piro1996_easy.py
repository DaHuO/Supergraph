#!/usr/bin/env python

import itertools

T = input()

for t in range(T):
    n, r, p, s = map(int, raw_input().split())
    st = 'P' * p + 'R' * r + 'S' * s

    for line in itertools.permutations(st):
        line = ''.join(line)
        res = line
        while len(line) != 1:
            nl = ''
            for i in range(0, len(line), 2):
                if line[i] == line[i + 1]:
                    break
                if line[i: i + 2] in ['PR', 'RP']:
                    nl += 'P'
                elif line[i: i + 2] in ['RS', 'SR']:
                    nl += 'R'
                elif line[i: i + 2] in ['SP', 'PS']:
                    nl += 'S'
            else:
                line = nl
                continue
            break
        else:
            print 'Case #%d: %s' % (t + 1, res)
            break
    else:
        print 'Case #%d: IMPOSSIBLE' % (t + 1)
