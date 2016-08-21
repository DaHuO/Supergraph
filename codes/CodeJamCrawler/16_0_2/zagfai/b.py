#!/usr/bin/python
# -*- coding: utf-8 -*-
""" solve
"""
__author__ = 'Zagfai'
__date__ = '2016-04'
__license__ = 'MIT'

def reverse(line, i):
    for j in range(i+1):
        if line[j] == '+':
            line[j] = '-'
        elif line[j] == '-':
            line[j] = '+'
    return list(reversed(line[:i+1])) + line[i+1:]

def solve():
    walks = 0
    line = list(raw_input().strip())

    last = len(line) - 1
    while last >= 0:
        if not '+' in line:
            walks += 1
            break
        if not '-' in line:
            break

        if line[0] == '+':
            for plus in range(last+1):
                if line[plus] != '+':
                    break
            else:
                plus += 1
            plus -= 1
            line = reverse(line, plus)
            walks += 1
        elif line[0] == '-':
            for minus in range(last, -1, -1):
                if line[minus] != '+':
                    break
            #print line, minus
            line = reverse(line, minus)
            walks += 1
            last = minus - 1

    return walks


n = int(raw_input())

for i in range(1, n+1):
    print "Case #%s: %s" % (i, solve())


