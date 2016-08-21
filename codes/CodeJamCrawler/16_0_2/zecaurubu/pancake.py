#!/usr/bin/env python3

import sys

def parse_pancake(string):
    return [x == '+' for x in list(string)]

def flip(arr):
    if all(arr):
        return 0

    i = 1
    current = arr[0]
    for b in arr[1:]:
        if b == current:
            pass
        else:
            current = b
            i = i + 1
    if arr[-1]:
        i = i - 1
    return i


with open(sys.argv[1],'rt') as infile, open("pancake.out",'wt') as outfile:
     ncases = int(infile.readline())
     i = 1
     for line in infile:
         stack = parse_pancake(line.strip())
         nflips = flip(stack)
         print("Case #{}: {}".format(i,nflips),file=outfile)
         i = i + 1
