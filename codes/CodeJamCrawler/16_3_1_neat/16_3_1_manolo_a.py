# coding=utf-8

# Created on 2016-05-08
# Code Jam 2016 - 1C - A
# @author: manolo


import sys
import operator

ifile = sys.stdin
ofile = sys.stdout


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


def solve(p):

    p_sorted = sorted(p.items(), key=operator.itemgetter(1), reverse=True)

    #print '---------------'
    #print p_sorted

    total = sum(p.values())

    if len(p_sorted) == 0:
        return ''
    elif len(p_sorted) == 1:
        return 'TRASH'
    else:
        first = p_sorted[0]
        first_name = first[0]
        second = p_sorted[1]
        second_name = second[0]

        p[first_name] = first[1] - 1
        if p[first_name] == 0:
            del p[first_name]

        if total % 2 == 1:
            return '{} {}'.format(first_name, solve(p))

        p[second_name] = second[1] - 1
        if p[second_name] == 0:
            del p[second_name]

        return '{}{} {}'.format(first_name, second_name, solve(p))

    #total = sum(a.values())
    #half = total / 2
    #majority = half + 1


A_PARTY_INT = ord('A')

T = int(r())
for case in range(1, T+1):
    n = int(r())
    ps = r().split(' ')
    parties = {}
    for i, p in enumerate(ps):
        parties[chr(A_PARTY_INT + i)] = int(p)
    what = solve(parties)
    w(case, what)

