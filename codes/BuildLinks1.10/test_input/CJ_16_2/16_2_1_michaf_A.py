#!/usr/bin/env python3

import sys, os, re
import collections
import math

sys.setrecursionlimit(200)

def debug(x):
    print(x, file=sys.stderr) 

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
lettertodigit = {}

def solve(d):
    ans = []
    freq = collections.defaultdict(int)
    for x in d:
        freq[x] += 1

    donedigits = []
    for k in lettertodigit:
        if len(lettertodigit[k]) == 1:
            donedigits.append(lettertodigit[k][0])
            minocc = float("inf") 
            for l in digits[lettertodigit[k][0]]:
                minocc = min(minocc, freq[l])
            if minocc > 0:
                for l in digits[lettertodigit[k][0]]:
                    freq[l] -= minocc
                ans.extend([lettertodigit[k][0]] * minocc)
#    {'H': [3, 8], 'G': [8], 'I': [5, 6, 8, 9], 'Z': [0], 'N': [1, 7, 9], 
#   'E': [0, 1, 3, 5, 7, 8, 9], 'T': [2, 3, 8], 'V': [5, 7], 'R': [0, 3, 4], 
#   'F': [4, 5], 'O': [0, 1, 2, 4], 'U': [4], 'W': [2], 'S': [6, 7], 'X': [6]}
    testletters = ['H', 'F', 'O', 'S', 'I'] 
    for t in testletters:
        num = freq[t]
        digit = [x for x in lettertodigit[t] if x not in donedigits][0]
        for k in digits[digit]:
            freq[k] -= num
        ans.extend([digit] * num)
        donedigits.append(digit)

    return "".join([str(x) for x in sorted(ans)])

def main():
    inp = [x.strip() for x in sys.stdin.readlines()]
    T = int(inp[0])
    D = inp[1:]

    debug(T)
    debug(D)

    #for i in range(ord('A'), ord('Z')):
    #    lettertodigit[chr(i)] = []

    for i, digit in enumerate(digits):
        for x in digit:
            if x not in lettertodigit:
                lettertodigit[x] = [i]
            else:
                if not i in lettertodigit[x]:
                    lettertodigit[x].append(i)

    debug(lettertodigit)

    for numinput, d in enumerate(D, 1):
        debug("d: %s" % d)
        ans = solve(d)
        print("Case #%d: %s" % (numinput, ans))

if __name__ == '__main__':
    main()
