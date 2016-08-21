#!/usr/bin/env python 
# -*- coding: utf-8 -*-
__author__ = 'duc_tin'


def flip(to=-1):
    S_new = ''
    mark = len(S) if to == -1 else to
    for c in S[0:mark]:
        S_new += '+' if c == '-' else '-'

    return S_new[::-1] + S[mark:len(S)]
#
#
# def last_same_char():
#     l = S.count('+')
#     if l:
#         plus = S.index('+')
#         while l:
#             longest = '+' * l
#             if longest in S:
#                 plus = S.index(longest) + l
#                 break
#
#             l-=1
#
#     m = S.count('-')
#     if m:
#         minus = S.index('-')
#         while m:
#             longest = '-' * m
#             if longest in S:
#                 minus = S.index(longest) + m
#                 break
#
#             m -= 1
#
#     if l and m:
#         if not minus - m and minus == plus - l:
#             return minus
#         elif not plus - l and plus == minus - m:
#             return plus
#
#     target = 0
#     if l > m:
#         target = plus
#     elif l < m:
#         target = minus
#     else:
#         target = min(plus, minus)
#
#     return target
#
#
# T = int(raw_input())
#
# for case in range(1, T + 1):
#     S = raw_input()
#     count = 0
#
#     while '-' in S:
#         count += 1
#         flip_upto = last_same_char()
#         S = flip(flip_upto)
#     else:
#         print 'Case #%d: %s' % (case, count)


T = int(raw_input())

for case in range(1, T + 1):
    S = raw_input()
    count = 0

    while '-' in S:
        if '+' in S and S[0] == '+':
            p = S.index('-')
            S = flip(p)
            count += 1
        elif '-' in S and S[0] == '-':
            if '+' in S:
                m = S.index('+')
                S = flip(m)
            else:
                S = flip()
            count += 1

    else:
        print 'Case #%d: %s' % (case, count)
