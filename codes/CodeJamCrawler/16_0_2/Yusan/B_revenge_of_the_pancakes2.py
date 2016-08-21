#!/usr/bin/python
# vi: set fileencoding=utf-8 :

'''
Google code jam 2016 qualification round
B: revenge of the pancakes
'''


def minimum_reverse_and_flip_minus(s):
    if len(s) <= 1:
        if s[0] == '-':
            return 0
        else:
            return 1
    if s[-1] == '-':
        return minimum_reverse_and_flip_minus(s[:-1])
    else:
        return minimum_reverse_and_flip(s[:-1]) + 1


def minimum_reverse_and_flip(s):
    if len(s) <= 1:
        if s[0] == '+':
            return 0
        else:
            return 1
    if s[-1] == '+':
        return minimum_reverse_and_flip(s[:-1])
    else:
        return minimum_reverse_and_flip_minus(s[:-1]) + 1


T = int(raw_input())
for case_number in range(1, T + 1):
    S = raw_input().rstrip()
    print 'Case #%d: %s' % (case_number, minimum_reverse_and_flip(S))
