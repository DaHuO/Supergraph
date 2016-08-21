#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Google Code Jam: Qualification Round 2016
# Problem B. Revenge of the Pancakes
#
# by xenosoz on Apr 10, 2016.
#

def solve(S):
    count = 0
    while True:
        last_blank_index = S.rfind('-')
        if last_blank_index == -1:
            # No blank side: we're happy now!
            return count
        
        # We don't care the happy bottom anymore.
        S = S[:last_blank_index+1]

        if S[0] == '+':
            # Flip all +'s that is in top of the stack.
            first_blank_index = S.find('-')
            S = '-' * first_blank_index + S[first_blank_index:]
            count += 1

        # Flip all.
        S = S[::-1].replace('-', '!').replace('+', '-').replace('!', '+')
        count += 1
        

T = int(input())

for case_number in range(1, T+1):
    S = input()
    print("Case #%d:" % case_number, solve(S))
