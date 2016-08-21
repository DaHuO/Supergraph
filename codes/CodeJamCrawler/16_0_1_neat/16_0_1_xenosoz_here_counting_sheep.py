#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Google Code Jam: Qualification Round 2016
# Problem A. Counting Sheep
#
# by xenosoz on Apr 10, 2016.
#

def solve(N):
    if N == 0:
        return "INSOMNIA"
    
    counter = set()
    number = 0
    while True:
        number += N
        counter.update(str(number))
        if len(counter) >= 10:
            return number

    
T = int(input())

for case_number in range(1, T+1):
    N = int(input())
    print("Case #%d:" % case_number, solve(N))
