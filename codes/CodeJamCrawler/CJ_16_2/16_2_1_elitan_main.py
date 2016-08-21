#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import copy
import time

numbers = [
    'ZERO',
    'ONE',
    'TWO',
    'THREE',
    'FOUR',
    'FIVE',
    'SIX',
    'SEVEN',
    'EIGHT',
    'NINE',
]

def nrins(n, s):
    stmp = s[0]
    # check if n substring exists in stmp
    for l in n:
        if l not in stmp:
            return False


    # place it back and return
    s[0] = stmp
    return True

def findnr(s, nr, current_n):
    if len(s[0]) == 0:
        return nr[0]

    global numbers
    for x in range(current_n, 10):
        if nrins(numbers[x], s):
            stmp = copy.deepcopy(s[0])
            nrtmp = copy.deepcopy(nr[0])
            # the substring exists in s, remove it.
            for l in numbers[x]:
                stmp = stmp.replace(l, '', 1)

            nrtmp += str(x)
            r = findnr([stmp], [nrtmp], current_n)
            if r:
                return r
    return False


def main():

    T = int(input())
    for i, tc in enumerate(range(T)):
        s = ['']
        nr = ['']
        s[0] = input()
        nr[0] = ''
        
        r = findnr(s, nr, 0)
        
        print('Case #%d: %s' % (i+1, r))

if __name__ == '__main__':
    main()
