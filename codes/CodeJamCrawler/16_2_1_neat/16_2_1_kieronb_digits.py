#!/usr/bin/python

import sys
#import logging

#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

nums = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'];

def solve(s):
    digits = []

    while 'Z' in s:
        digits.append(0)
        s = remove_word(s, nums[0])

    while 'W' in s:
        digits.append(2)
        s = remove_word(s, nums[2])

    while 'U' in s:
        digits.append(4)
        s = remove_word(s, nums[4])

    while 'X' in s:
        digits.append(6)
        s = remove_word(s, nums[6])
    
    while 'G' in s:
        digits.append(8)
        s = remove_word(s, nums[8])

    while 'O' in s:
        digits.append(1)
        s = remove_word(s, nums[1])

    while 'R' in s:
        digits.append(3)
        s = remove_word(s, nums[3])
    
    while 'F' in s:
        digits.append(5)
        s = remove_word(s, nums[5])

    while 'V' in s:
        digits.append(7)
        s = remove_word(s, nums[7])
    
    while 'N' in s:
        digits.append(9)
        s = remove_word(s, nums[9])

    return ''.join(sorted([str(i) for i in digits]))

def remove_word(s, w):
    for c in w:
        s = remove_char(s, c)
    return s

def remove_char(s, c):
    if not c in s:
        return s
    i = s.index(c)
    return s[:i] + s[i+1:]

first = True
n = 0
for line in sys.stdin:
    if first:
        first = False
    else:
        n = n + 1
        ans = solve(line)
        print("Case #" + str(n) + ": " + ans)
