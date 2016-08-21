#!/usr/bin/env python 
# -*- coding: utf-8 -*-
__author__ = 'duc_tin'


def get_largest():
    return [party for party in book if book[party]==max(book.values())]


parties = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

T = int(raw_input())

for case in range(1, T + 1):
    res = ''
    N = int(raw_input())
    P = map(int, raw_input().split())
    book = dict(zip(parties[:N], P))

    while any(book.values()):
        sort_p = sorted(book, key=lambda x:book[x], reverse=True)
        p1, p2 = sort_p[:2]
        if book[p1]==book[p2]:
            book[p1] -= 1
            book[p2] -= 1

            m = max(book.values())
            if m > sum(book.values())/2.:
                book[p2] += 1
                res += p1 + ' '
            else:
                res += p1+p2+' '
        elif len([x for x in book if book[x]>0]) > 2:
            book[p1] -= 2
            res += p1 + p1 + ' '
        else:
            book[p1] -= 1
            res += p1 + ' '
    print 'Case #%d: %s' % (case, res)