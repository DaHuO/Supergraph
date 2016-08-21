#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations_with_replacement

def solve(inp):
    inp = ''.join(sorted(inp))
    nums = [(0, "ZERO"),
            (1, "ONE"),
            (2, "TWO"),
            (3, "THREE"),
            (4, "FOUR"),
            (5, "FIVE"),
            (6, "SIX"),
            (7, "SEVEN"),
            (8, "EIGHT"),
            (9, "NINE")]
    strings = list(combinations_with_replacement(nums,6))
    strings += list(combinations_with_replacement(nums,5))
    strings += list(combinations_with_replacement(nums,4))
    strings += list(combinations_with_replacement(nums,3))
    strings += list(combinations_with_replacement(nums,2))
    strings += list(combinations_with_replacement(nums,1))
    numsAndStrings = map(makePhoneNumber, strings)
    for (nums, string) in numsAndStrings:
        if inp == string:
            return ''.join(str(e) for e in nums)

def makePhoneNumber(words):
    nums = []
    string = ""
    for (num, word) in words:
        nums.append(num)
        string += word
    return (nums, ''.join(sorted(string)))

if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
