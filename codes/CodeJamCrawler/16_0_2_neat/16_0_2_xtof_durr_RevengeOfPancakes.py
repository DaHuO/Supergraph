#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# google code jam - c.durr - 2016
# Revenge Of Pancakes
# greedy, complexity O(n) -- why is input only n<=100 ? suspicious

from sys import stdin


def readint(): return int(stdin.readline())
def readints(): return list(map(int, stdin.readline().split()))
def readstr(): return stdin.readline().strip()


def solve(pancakes):
    answer = 0
    n = len(pancakes)
    pancakes += '+'
    for i in range(n):
        if pancakes[i] != pancakes[i+1]:
            answer += 1
    return answer

for test in range(readint()):
    print('Case #%d: %s' % (test+1, solve(readstr())))

